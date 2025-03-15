from abc import ABC, abstractmethod
from typing import Optional, Union
from pydantic import BaseModel
from llama_index.core.prompts import PromptTemplate
from app.domain.interfaces.base_llm import BaseLLM
from app.domain.models.resume import Resume


class BaseParser(ABC):
    def __init__(
        self,
        llm: Optional[Union[BaseLLM]] = None,
        model: Optional[BaseModel] = None,
        prompts: Optional[PromptTemplate] = None,
        file_path: Optional[str] = None,
        file_bytes: Optional[bytes] = None,
    ):
        if not file_path and not file_bytes:
            raise ValueError("File path or file must be provided.")
        self.file_path = file_path
        self.file = file_bytes
        self.llm = llm
        self.model = model
        self.prompt = prompts

    @abstractmethod
    def extract_text(self) -> str:
        pass

    @abstractmethod
    def extract_to_object(self) -> Resume:
        pass
