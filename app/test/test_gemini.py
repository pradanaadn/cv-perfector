from loguru import logger
from pprint import pprint
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
        (
            "You are an expert in extract markdown text to a python class or pydantic BaseModel\n"
            "Only extract relevant information from the {text}, that is a markdown from a resume\n"
            "If you do not know the value of an attribute asked to extract, return None for the attribute's value."
            "If there information about soft skill, technical skill, language proficiency pass it to Skill class"
        )
    )
    async with aiofiles.open(
        "documents/markdown/output.md", "r"
    ) as file:
        text = await file.read()
    response = llm.structure_predict(Resume, prompt, text)

    pprint(response)


if __name__ == "__main__":
    asyncio.run(test_structure_output())
