import pytest
from app.infrastructure.parser.pdf.pdf_parser import PDFParser 
from pydantic import BaseModel

FILE_PATH = "documents/resume/functionalsample.pdf"
EMPTY_FILE_PATH = "documents/resume/empty.pdf"
CORRUPTED_FILE_PATH = "documents/resume/corrupted.pdf"
NON_PDF_FILE_PATH = "documents/resume/not_a_pdf.txt"

class MockLLM:
    def structure_predict(self, model_output, prompts, text):
        return model_output.parse_obj({"text": text})

class MockModel(BaseModel):
    text: str

class MockPromptTemplate:
    pass

def test_pdf_parser_path():
    pdf_parser = PDFParser(file_path=FILE_PATH)
    markdown_text = pdf_parser.extract_text()
    assert markdown_text != '', "The extracted text is empty."

def test_pdf_parser_byte():
    with open(FILE_PATH, 'rb') as f:
        pdf = f.read()
    pdf_parser = PDFParser(file_bytes=pdf)
    markdown_text = pdf_parser.extract_text()
    assert markdown_text != '', "The extracted text is empty."

def test_empty_pdf():
    pdf_parser = PDFParser(file_path=EMPTY_FILE_PATH)
    markdown_text = pdf_parser.extract_text()
    assert markdown_text.strip() == "-----", f"The extracted text should be empty for an empty PDF, got {markdown_text}"


def test_non_pdf_file():
    pdf_parser = PDFParser(file_path=NON_PDF_FILE_PATH)
    with pytest.raises(Exception):
        pdf_parser.extract_text()

def test_missing_file_path_and_file():
    with pytest.raises(ValueError, match="File path or file must be provided."):
        pdf_parser = PDFParser()
        pdf_parser.extract_text()

def test_extract_to_object():
    pdf_parser = PDFParser(
        file_path=FILE_PATH,
        llm=MockLLM(),
        model=MockModel,
        prompts=MockPromptTemplate()
    )
    object_model = pdf_parser.extract_to_object()
    assert object_model.text != '', "The extracted object model text is empty."

def test_missing_llm_model_prompt():
    pdf_parser = PDFParser(file_path=FILE_PATH)
    with pytest.raises(ValueError, match="Model, LLM, and Prompt must be provided."):
        pdf_parser.extract_to_object()