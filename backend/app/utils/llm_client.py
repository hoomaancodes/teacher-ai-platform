from groq import Groq

from app.config.settings import (
    GROQ_API_KEY,
    MODEL_NAME
)


class LLMClient:

    def __init__(self):
        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def generate(self, prompt: str, content: str):

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
            temperature=0.2,
            response_format={"type": "json_object"}
        )

        return response.choices[0].message.content