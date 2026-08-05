from app.models import ChatResponse
from app.services.database_service import DatabaseService
from app.services.response_generator import ResponseGenerationService
from app.services.sql_generator import SQLGenerationService
from app.services.sql_validator import SQLValidatorService


class ChatService:
    def __init__(self):
        self.sql_generator = SQLGenerationService()

    def process_message(self, conversation_id, message, user_id):
        sql_query = self.sql_generator.generate_sql(
            user_question=message, conversation_id=conversation_id, user_id=user_id
        )
        sql_query = sql_query.strip()  # Remove trailing whitespace if present

        # Validate the generated SQL
        validation_result = SQLValidatorService.validate(sql_query)
        if not validation_result.is_valid:
            return ChatResponse(
                user_id=user_id,
                conversation_id=conversation_id,
                response=f"Generated SQL is invalid: {validation_result.error}",
            )
        query_response = DatabaseService().execute_query(sql_query)

        if not query_response:
            return ChatResponse(
                conversation_id=conversation_id,
                user_id=user_id,
                response=f"Generated SQL: {sql_query}, \n Query Response: No matching data was found.",
            )

        else:
            nlm_response = ResponseGenerationService().generate_response(
                user_question=message, sql_query=sql_query, sql_result=query_response
            )
            if not nlm_response:
                return ChatResponse(
                    conversation_id=conversation_id,
                    user_id=user_id,
                    response=f"Generated SQL: {sql_query}, \n Query Response: No matching data was found.",
                )

            else:
                return ChatResponse(
                    conversation_id=conversation_id,
                    user_id=user_id,
                    response=f"Generated SQL: {sql_query}, \n Query Response: {nlm_response}.",
                )
