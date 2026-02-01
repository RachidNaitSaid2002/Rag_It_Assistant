from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    isactive: Optional[str] = "active"

class loginBase(BaseModel):
    email: str
    hashedpassword: str

class UserCreate(UserBase):
    hashedpassword: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
