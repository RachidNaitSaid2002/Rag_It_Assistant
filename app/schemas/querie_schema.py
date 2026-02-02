from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class QueryBase(BaseModel):
    user_id: int
    question: str
    answer: Optional[str] = None
    cluster: Optional[int]
    latency_ms: Optional[float] = None
    formatted_sources: Optional[list] = None

class QueryCreate(QueryBase):
    pass

class Query(QueryBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)