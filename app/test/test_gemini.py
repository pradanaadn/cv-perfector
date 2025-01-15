from loguru import logger
import asyncio
from pydantic import BaseModel
import aiofiles
from llama_index.core.prompts import PromptTemplate
from app.infrastructure.llm.models.gemini import GeminiLlamaIndex
from app.domain.models.resume import Resume


async def test_async_complete():
    llm = GeminiLlamaIndex()
    resp = await llm.async_complete("Buatkan puisi")

    async for response in resp:
        print(response, end="", flush=True)


async def test_structure_output():
    llm = GeminiLlamaIndex()
    prompt = PromptTemplate(
        "You are an expert extraction algorithm. Only extract relevant information from the {text}. If you do not know the value of an attribute asked to extract, return null for the attribute's value."
    )
    async with aiofiles.open("documents/markdown/Putu_Gede_Pradana_Adnyana_CV.md", "r") as file:
        text = await file.read()
    response = llm.structure_predict(Resume, prompt, text)
    
    print(response, type(response))

if __name__ == "__main__":
    asyncio.run(test_structure_output())
