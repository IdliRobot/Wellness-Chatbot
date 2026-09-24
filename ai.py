from os import environ
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key: str = environ.get("GROQ_API_KEY")

instructions: str = open("instructions.txt").read()
disclaimer: str = open("disclaimer.txt").read()
welcome: str = open("welcome.txt").read()

prompt: dict = {
    "role": "system",
    "content": instructions
}

class Chat:
    def __init__(self):
        self.history: list[dict] = [prompt]
        self.client: Groq = Groq(api_key = api_key)

    def message(self, message: str) -> str:
        message += "\n\n" + instructions
        user: dict = {
            "role": "user",
            "content": message
        }
        self.history.append(user)
    
        response = self.client.chat.completions.create(model = "openai/gpt-oss-20b", messages = self.history)
        answer: str = response.choices[0].message.content
        reply: dict = {
            "role": "assistant",
            "content": answer
        }
        self.history.append(reply)
        return f"{answer}\n-# {disclaimer}"