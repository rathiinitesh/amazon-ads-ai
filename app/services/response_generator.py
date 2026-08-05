from app.services.client import OpenAIClient
from app.utils import PromptLoader


class ResponseGenerationService:
    def __init__(self):
        self.openai = OpenAIClient()

    def generate_response(
        self,
        user_question: str,
        sql_query: str,
        sql_result: list[dict],
    ) -> str:
        prompt = f"""
User Question:
{user_question}

Executed SQL:
{sql_query}

SQL Result:
{sql_result}

Write a concise business-friendly answer.
"""

        system_prompt = "\n\n".join(
            [
                PromptLoader.load("system/nl_role_rules.txt"),
                PromptLoader.load("system/database_schema.txt"),
                PromptLoader.load("system/business_rules.txt"),
            ]
        )
        messages = [
            {
                "role": "system",
                "content": system_prompt,
            },
            {"role": "user", "content": prompt},
        ]

        return self.openai.chat_completion_create(messages=messages)
