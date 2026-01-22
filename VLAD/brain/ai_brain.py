from openai import OpenAI
import os

class AIBrain:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def think(self, command: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are VLAD, a powerful personal AI assistant."},
                    {"role": "user", "content": command}
                ],
                temperature=0.4
            )
            return response.choices[0].message.content.strip()

        except Exception:
            return "I encountered an error while thinking."
