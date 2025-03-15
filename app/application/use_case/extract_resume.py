from typing import Optional

from llama_index.core.prompts import PromptTemplate
from app.domain.interfaces.base_parser import BaseParser
from app.domain.interfaces.base_llm import BaseLLM
from app.domain.models.resume import Resume


class ExtractResumeUseCase:
    def __init__(
        self, parser: BaseParser, llm: BaseLLM, extraction_prompt: PromptTemplate
    ):
        self.parser = parser
        self.llm = llm
        self.prompt = extraction_prompt

    async def execute(
        self, file_path: Optional[str] = None, file_bytes: Optional[bytes] = None
    ) -> Resume:
        parser = self.parser(
            llm=self.llm,
            model=Resume,
            prompts=self.prompt,
            file_path=file_path,
            file_bytes=file_bytes,
        )
        resume = parser.extract_to_object()
        return resume
