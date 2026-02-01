from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from app.db.db_connection import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String)
    hashedpassword = Column(String)
    isactive = Column(String, default="active")
    created_at = Column(DateTime, server_default=func.now())

    queries = relationship("Queryies", back_populates="user")