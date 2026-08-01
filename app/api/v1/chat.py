from fastapi import APIRouter

from app.models import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


@router.post("/chat")
async def chat(request: ChatRequest):
    return chat_service.process_message(
        conversation_id=request.conversation_id,
        message=request.message,
    )
