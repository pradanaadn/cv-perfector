from abc import ABC, abstractmethod
from app.domain.models.resume import Resume

class BaseParser(ABC):
    @abstractmethod
    def extract_text(cls) -> str:
        pass

    @abstractmethod
    def extract_to_object(cls) -> Resume:
        pass