from llama_index.llms.gemini import Gemini
from llama_index.core.program.llm_program import LLMTextCompletionProgram
from llama_index.core.llms import CustomLLM
from pydantic import BaseModel
from typing import Union
from app.core.config import secret, GeminiModel, gemini_model


class GeminiLlamaIndex:
    """
    A class to interact with the Gemini LLM (Large Language Model) for text completion and structured prediction.
    Attributes:
        model (Union[GeminiModel, str]): The Gemini model instance or model name.
        api_key (str): The API key for accessing the Gemini service.
        llm (CustomLLM): An instance of the Gemini LLM.
    Methods:
        complete(prompt: str) -> str:
            Completes the given prompt using the Gemini LLM.
        async_complete(prompt: str) -> str:
            Asynchronously completes the given prompt using the Gemini LLM.
        structure_predict(model_output: BaseModel, prompt: str, text: str) -> BaseModel:
            Generates a structured prediction based on the given prompt and text using the Gemini LLM.
    """
    def __init__(self, model: Union[GeminiModel, str]= None, api_key: str = None):
        self.model = model or gemini_model.model
        self.api_key = api_key or secret.services.get("LLM").config.get("gemini")
        self.llm:CustomLLM = Gemini(model=self.model, api_key=self.api_key)
        
    def complete(cls, prompt: str):
        llm_response = cls.llm.complete(prompt)
        return llm_response
    
    async def async_complete(cls, prompt: str):
        llm_response =  await cls.llm.acomplete(prompt)
        return llm_response
    
    def structure_predict(cls, model_output:BaseModel,  prompt: str, text:str,):
        textCompletion = LLMTextCompletionProgram.from_defaults(
            output_cls=model_output,
            prompt_template_str=prompt,
            llm=cls.llm,
        )
        llm_output = textCompletion.run(text=text)
        return llm_output

