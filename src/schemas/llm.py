from pydantic.dataclasses import dataclass
from pydantic import Field
from typing import Union, Literal


@dataclass
class GeminiConfig:
    """Configuration parameters for generating responses from a Gemini model.

    Attributes:
        temperature (Union[int, float]): Controls the randomness of the generated text.  Higher values (closer to 2)
            result in more random output, while lower values (closer to 0) make the output more deterministic. Must be
            between 0 and 2 inclusive. Defaults to 1.
        top_p (Union[int, float]): Controls the diversity of the generated text using nucleus sampling. At each step,
            only tokens whose cumulative probability exceeds `top_p` are considered.  Must be between 0 and 1 inclusive.
            Defaults to 0.95.
        top_k (int): Controls the diversity of the generated text using top-k sampling. At each step, only the `top_k` most
            likely tokens are considered. Must be greater than or equal to 1. Defaults to 40.
        max_token (int): The maximum number of tokens to generate in the response. Must be between 0 and 10,000
            inclusive. Defaults to 5,000.
        response_mime_type (Literal["text/plain", "application/json"]): The MIME type of the response.  Can be either
            "text/plain" for plain text or "application/json" for JSON. Defaults to "application/json".

    Instantiation:
     .. code-block:: python
        llm_config = GeminiConfig(
        temperature = 0.5,
        top_p = 0.98,
        top_k = 20,
        max_token = 1000,
        response_mime_type = "text/plain" )

    or you can just use the default value,
     .. code-block:: python
        llm_config = GeminiConfig()
    """

    temperature: Union[int, float] = Field(ge=0, le=2, default=1)
    top_p: Union[int, float] = Field(ge=0, le=1, default=0.95)
    top_k: int = Field(ge=1, default=40)
    max_token: int = Field(ge=0, le=10_000, default=5_000)
    response_mime_type: Literal["text/plain", "application/json"] = Field(
        default="application/json"
    )
