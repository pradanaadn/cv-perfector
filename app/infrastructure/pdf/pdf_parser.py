import pymupdf4llm 
from typing import Union
from langchain.llms.base import BaseLanguageModel, BaseLLM
class PDFParser:
    def __init__(self, file_path:str, llm:Union[BaseLLM, BaseLanguageModel]):
        self.file_path = file_path
        self.llm = llm
        
    def extract_text(self)->str:
        md_text = pymupdf4llm.to_markdown(self.file_path)
        return md_text
    def extract_to_object(self):
        pass