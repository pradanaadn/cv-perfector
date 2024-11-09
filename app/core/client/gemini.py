from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel

class ChatGemini(BaseModel):
    def __init__(self, model:str):
        self.model = model
        self