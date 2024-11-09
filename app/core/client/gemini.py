from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from app.schemas.llm import GeminiConfig
from app.core.config import GEMINI_API_KEY


class ChatGemini(BaseModel):
    def __init__(
        self,
        model: str = "gemini-1.5-flash",
        config: GeminiConfig = GeminiConfig(),
        api_key: str = GEMINI_API_KEY,
    ):
        self.model = model
        self.config = config
        self.api_key = api_key
    def _init_llm(self):
        llm = ChatGoogleGenerativeAI(
            model=self.model,
            temperature=self.config.temperature,
            top_k=self.config.top_k,
            top_p=self.config.top_p,
            max_tokens=self.config.max_token,
            response_mime_type=self.config.response_mime_type,
            gemini_api_key = self.api_key
        )
        return llm