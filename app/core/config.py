from yaml import load, SafeLoader
from loguru import logger

try:
    with open("secret.yaml", "r") as file:
        credential = load(file, Loader=SafeLoader)

    GEMINI_API_KEY = credential["llm_key"]["gemini"]

except Exception as e:
    logger.exception(e)


