from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from app.schemas.llm import GeminiConfig
from app.core.config import GEMINI_API_KEY


class ChatGemini:
    def __init__(
        self,
        model: str = "gemini-pro",
        config: GeminiConfig = GeminiConfig(),
        api_key: str = GEMINI_API_KEY,
    ):
        self.model = model
        self.config = config
        self.api_key = api_key
        self.llm = self._init_llm()

    def _init_llm(self):
        llm = ChatGoogleGenerativeAI(
            model=self.model,
            temperature=self.config.temperature,
            top_k=self.config.top_k,
            top_p=self.config.top_p,
            max_tokens=self.config.max_token,
            response_mime_type=self.config.response_mime_type,
            google_api_key=self.api_key,
        )
        return llm

    def invoke_message(self, message: str):
        result = self.llm.invoke(message)
        return result


if __name__ == "__main__":
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro", temperature=0.7, top_p=0.85, google_api_key=GEMINI_API_KEY
    )
    llm2 = ChatGemini()
    
    result = llm.invoke("Halo")
    result2 = llm2.invoke_message("Halo")
    
    print(result, result2)
