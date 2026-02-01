from fastapi import APIRouter, HTTPException, status, Depends
from datetime import timedelta
from sqlalchemy.orm import Session

from app.auth.token_auth import create_access_token
from app.core.config import settings
from app.db.db_connection import get_db_session as get_db
from app.models.user_model import User
from app.schemas.users_schema import loginBase
from app.schemas.token_schema import Token


router = APIRouter(prefix="/auth", tags=["Login"])


@router.post("/login", response_model=Token)
def login(request: loginBase, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()

    if not user or user.hashedpassword != request.hashedpassword:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nom d'utilisateur ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "sub": user.username,
            "user_id": user.id
        },
        expires_delta=access_token_expires
    )

    return {
        "message": "Login réussi",
        "access_token": access_token,
    }