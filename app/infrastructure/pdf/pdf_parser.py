import pymupdf4llm 
from typing import Union
from pydantic import BaseModel
from llama_index.core.prompts import PromptTemplate
from app.domain.interfaces.base_parser import BaseParser
from app.domain.interfaces.base_llm import BaseLLM
class PDFParser(BaseParser):
    """
    A class used to parse PDF files and extract structured data using a language model.

    Attributes
    ----------
    file_path : str
        The path to the PDF file to be parsed.
    llm : Union[BaseLLM]
        The language model used for structuring the extracted text.
    model : BaseModel
        The model used to predict the structure of the extracted text.
    prompt : PromptTemplate
        The prompt template used for guiding the language model.

    Methods
    -------
    extract_text() -> str
        Extracts text from the PDF file and converts it to markdown format.
    extract_to_object() -> BaseModel
        Extracts text from the PDF file, converts it to markdown format, and then structures it into an object model using the language model.
    """
    def __init__(self, file_path: str, llm: Union[BaseLLM],  model:BaseModel, prompts:PromptTemplate):
        self.file_path = file_path
        self.llm = llm
        self.model = model
        self.prompt = prompts

    def extract_text(cls) -> str:
        md_text = pymupdf4llm.to_markdown(cls.file_path)
        return md_text

    def extract_to_object(cls) -> BaseModel:
        md_text = cls.extract_text()
        object_model = cls.llm.structure_predict(model_output=cls.model, prompts=cls.prompt, text=md_text)
        return object_model
