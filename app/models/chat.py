from pydantic import BaseModel


class ChatRequest(BaseModel):
    conversation_id: int | None = None
    user_id: int
    message: str


class ChatResponse(BaseModel):
    user_id: int
    conversation_id: int | None = None
    response: str
