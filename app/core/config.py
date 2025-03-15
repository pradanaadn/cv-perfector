from pydantic import BaseModel, Field
from typing import Dict, Any, Literal
import yaml


class GeminiModel(BaseModel):
    model: Literal[
        "models/gemini-2.0-flash-exp",
        "models/gemini-1.5-flash",
        "models/gemini-1.5-flash-latest",
        "models/gemini-pro",
        "models/gemini-pro-latest",
        "models/gemini-1.5-pro",
        "models/gemini-1.5-pro-latest",
        "models/gemini-1.0-pro",
    ] = Field(
        default="models/gemini-2.0-flash-exp",
        description="The model of the Gemini LLM.",
    )


class ServiceConfig(BaseModel):
    config: Dict[str, Any]


class Secret(BaseModel):
    services: Dict[str, ServiceConfig]


def load_config(file_path: str) -> Secret:
    with open(file_path, "r") as file:
        config_dict = yaml.safe_load(file)
    return Secret(services={k: ServiceConfig(config=v) for k, v in config_dict.items()})


secret: Secret = load_config("secrets.yaml")
gemini_model = GeminiModel()