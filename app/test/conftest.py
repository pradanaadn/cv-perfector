from pytest import fixture
from llama_index.core.prompts import PromptTemplate
from app.infrastructure.llm.models.gemini import GeminiLlamaIndex
from app.infrastructure.llm.prompts.extraction_expert import RESUME_EXTRACTOR


@fixture
def llm_gemini():
    return GeminiLlamaIndex()


@fixture
def pdf_resume_path():
    return "documents/resume/functionalsample.pdf"


@fixture
def resume_extraction_template():
    return PromptTemplate(RESUME_EXTRACTOR)
