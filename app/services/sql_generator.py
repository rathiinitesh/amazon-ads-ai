from app.api.v1.utils import create_message, get_message_by_id
from app.api.v1.utils.conversation import create_conversation, update_conversation
from app.services.client import OpenAIClient
from app.utils import PromptLoader


class SQLGenerationService:
    def __init__(self):
        self.openai = OpenAIClient()
        self.system_prompt = "\n\n".join(
            [
                PromptLoader.load("system/role.txt"),
                PromptLoader.load("system/database_schema.txt"),
                PromptLoader.load("system/business_rules.txt"),
                PromptLoader.load("system/output_format.txt"),
            ]
        )

    def generate_sql(
        self, user_question: str, conversation_id: int | None, user_id: int
    ):
        if conversation_id is None:
            conversation = create_conversation(
                user_id=user_id, title=str(user_question[:100])
            )
            conversation_id = conversation.conversation_id
        else:
            conversation = update_conversation(
                conversation_id=conversation_id,
                user_id=user_id,
                title=str(user_question[:100]),
            )
            conversation_id = conversation.conversation_id
            if conversation is None:
                raise ValueError(
                    "Conversation not found or user does not have permission to update it."
                )

        db_messages = get_message_by_id(
            conversation_id=conversation_id, sort_by="created_at", sort_order="desc"
        )

        previous_messages = []
        if db_messages:
            previous_messages.append(
                {
                    "role": db_messages.role,
                    "content": db_messages.content,
                }
            )

        _ = create_message(
            conversation_id=conversation_id,
            role="user",
            content=user_question,
            message_order=len(previous_messages) + 1,
        )

        messages = (
            [
                {
                    "role": "system",
                    "content": self.system_prompt,
                }
            ]
            + previous_messages
            + [
                {
                    "role": "user",
                    "content": user_question,
                },
            ]
        )

        response_content = self.openai.chat_completion_create(messages)
        _ = create_message(
            conversation_id=conversation_id,
            role="assistant",
            content=response_content,
            message_order=len(previous_messages) + 2,
        )

        return response_content
