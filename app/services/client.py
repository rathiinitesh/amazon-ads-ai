from openai import OpenAI

from app.config import settings


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def chat_completion_create(self, messages, model="gpt-4-turbo"):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
        )

        return response.choices[0].message.content
