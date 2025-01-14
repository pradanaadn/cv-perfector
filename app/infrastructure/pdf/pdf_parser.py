import pymupdf4llm 
from typing import Union
from langchain.llms.base import BaseLanguageModel, BaseLLM
from llama_index.core.llms import CustomLLM
from app.domain.models.resume import Resume
from app.domain.interfaces.file_parser import BaseParser

class PDFParser(BaseParser):
    def __init__(self, file_path: str, llm: Union[BaseLLM, BaseLanguageModel, CustomLLM]):
        self.file_path = file_path
        self.llm = llm

    def extract_text(self) -> str:
        md_text = pymupdf4llm.to_markdown(self.file_path)
        return md_text

    def extract_to_object(self) -> Resume:
        md_text = self.extract_text()
        return md_text
