from typing import Union, Optional
from pydantic import BaseModel
from llama_index.core.prompts import PromptTemplate
from app.domain.interfaces.base_parser import BaseParser
from app.domain.interfaces.base_llm import BaseLLM
import fitz  # PyMuPDF
import pymupdf4llm


class PDFParser(BaseParser):
    """
    Initializes the PDF parser with the given parameters.
    Args:
        llm (Union[BaseLLM], optional): The language model to be used. Defaults to None.
        model (BaseModel, optional): The model to be used. Defaults to None.
        prompts (PromptTemplate, optional): The prompt templates to be used. Defaults to None.
        file_path (str, optional): The path to the PDF file. Defaults to None.
        file (bytes, optional): The PDF file in bytes. Defaults to None.
    Raises:
        ValueError: If neither file_path nor file is provided.
    """

    def __init__(
        self,
        llm: Optional[Union[BaseLLM]] = None,
        model: Optional[BaseModel] = None,
        prompts: Optional[PromptTemplate] = None,
        file_path: Optional[str] = None,
        file: Optional[bytes] = None,
    ):
        if not file_path and not file:
            raise ValueError("File path or file must be provided.")
        self.file_path = file_path
        self.file = file
        self.llm = llm
        self.model = model
        self.prompt = prompts

    def extract_text(self) -> str:
        file_document = self.byte_or_path()
        try:
            md_text = pymupdf4llm.to_markdown(file_document)

            if md_text.strip() == "":
                return ""
            return md_text
        except Exception as e:
            raise Exception("Failed to extract text from PDF") from e

    def byte_or_path(self):
        if self.file_path:
            return self.file_path
        elif self.file:
            return fitz.open(stream=self.file, filetype="pdf")
        else:
            raise ValueError("File path or file must be provided.")

    def extract_to_object(self) -> BaseModel:
        if not self.llm or not self.model or not self.prompt:
            raise ValueError("Model, LLM, and Prompt must be provided.")
        text = self.extract_text()
        return self.llm.structure_predict(self.model, self.prompt, text)
