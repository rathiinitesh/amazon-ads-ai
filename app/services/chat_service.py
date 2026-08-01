from app.models import ChatResponse


class ChatService:
    def process_message(self, conversation_id, message):
        return ChatResponse(
            conversation_id=conversation_id, response=f"You asked: {message}"
        )
