import pytest
from app.application.use_case.extract_resume import ExtractResumeUseCase
from app.infrastructure.parser.pdf import PDFParser

@pytest.mark.asyncio
async def test_with_pdf_parser(pdf_resume_path, llm_gemini, resume_extraction_template):
    extraction_usecase = ExtractResumeUseCase(
        parser=PDFParser, llm=llm_gemini, extraction_prompt=resume_extraction_template
    )
    resume= await extraction_usecase.execute(file_path=pdf_resume_path)
    assert False, f"{resume}"