from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.db.db_connection import get_db_session
from app.schemas.querie_schema import Query
from app.auth.token_auth import get_current_user
from app.models.queries_model import Queryies

router = APIRouter(prefix="/history", tags=["History"])

@router.get("/history", response_model=list[Query])
def get_history(db: Session = Depends(get_db_session), user_id: int = Depends(get_current_user)):
    history = db.query(Queryies).filter(Queryies.user_id == user_id).all()
    return history