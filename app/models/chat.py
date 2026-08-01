from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    conversation_id: Optional[int] = None
    message: str


class ChatResponse(BaseModel):
    conversation_id: Optional[int]
    response: str
