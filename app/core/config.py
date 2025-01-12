from pydantic import BaseModel
from typing import Dict, Any
import yaml

class ServiceConfig(BaseModel):
    config: Dict[str, Any]

class Config(BaseModel):
    services: Dict[str, ServiceConfig]

def load_config(file_path: str) -> Config:
    with open(file_path, 'r') as file:
        config_dict = yaml.safe_load(file)
    return Config(services={k: ServiceConfig(config=v) for k, v in config_dict.items()})

config:Config = load_config('secrets.yaml')

print(config)