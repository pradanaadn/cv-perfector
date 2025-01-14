
from loguru import logger
from app.infrastructure.llm.models.gemini import GeminiLlamaIndex
def main():
    llm = GeminiLlamaIndex()
    resp = llm.complete("Berapa 10 dikali 60?")
    logger.info((resp))

if __name__ == "__main__":
    main()

