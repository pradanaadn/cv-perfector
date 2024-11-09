from pydantic.dataclasses import dataclass
from pydantic import Field
from typing import Union, Literal


@dataclass
class GeminiConfig:
    temperature: Union[int, float] = Field(ge=0, le=2, default=1)
    top_p: Union[int, float] = Field(ge=0, le=1, default=0.95)
    top_k: int = Field(ge=1, default=40)
    max_token = Field(ge=0, le=10_000, default=5_000)
    response_mime_type: Literal["text/plain", "application/json"] = Field(
        default="application/json"
    )
