from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.db_connection import Base

class Queryies(Base):
    __tablename__ = "queryies"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=True)
    cluster = Column(Integer, nullable=True, default=0)
    latency_ms = Column(Float, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    formatted_sources = Column(JSON, nullable=True)

    user = relationship("User", back_populates="queries")