import asyncio
import datetime
from rich import print as rprint
from llama_index.core.prompts import PromptTemplate
from app.application.use_case.extract_resume import ExtractResumeUseCase
from app.infrastructure.parser.pdf import PDFParser
from app.infrastructure.llm.models.gemini import GeminiLlamaIndex
from app.infrastructure.llm.prompts.extraction_expert import RESUME_EXTRACTOR

async def main():
    llm = GeminiLlamaIndex()
    document_path = "documents/resume/CV_AI_PRADANA.pdf"
    prompt_template = PromptTemplate(RESUME_EXTRACTOR)
    extraction = ExtractResumeUseCase(parser=PDFParser, llm=llm,extraction_prompt=prompt_template)
    resume = await extraction.execute(file_path=document_path)
    rprint(resume)
    rprint(resume.education[0].end_date)
if __name__ == "__main__":
    asyncio.run(main())