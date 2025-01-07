from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import GEMINI_API_KEY
from app.schemas.llm import GeminiConfig


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
        self.llm = self.__init_llm()

    def __init_llm(self):
        llm = ChatGoogleGenerativeAI(
            model=self.model,
            temperature=self.config.temperature,
            top_k=self.config.top_k,
            top_p=self.config.top_p,
            max_tokens=self.config.max_token,

        )
        return llm

    def invoke_message(self, message: str):
        result = self.llm.invoke(message)
        return result


if __name__ == "__main__":

    llm2 = ChatGemini()


    result2 = llm2.invoke_message("Halo")

    print(result2)
