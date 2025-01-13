from pydantic import BaseModel
from typing import Dict, Any
import yaml

class ServiceConfig(BaseModel):
    config: Dict[str, Any]

class Secret(BaseModel):
    services: Dict[str, ServiceConfig]

def load_config(file_path: str) -> Secret:
    with open(file_path, 'r') as file:
        config_dict = yaml.safe_load(file)
    return Secret(services={k: ServiceConfig(config=v) for k, v in config_dict.items()})

secret:Secret = load_config('secrets.yaml')

