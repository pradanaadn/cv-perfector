from abc import ABC, abstractmethod
from pydantic import BaseModel
from llama_index.core.prompts import PromptTemplate


class BaseLLM(ABC):
    @abstractmethod
    def structure_predict(
        cls,
        model_output: BaseModel,
        prompts: PromptTemplate,
        text: str,
    ) -> BaseModel:
        pass
