from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from app.domain.models.resume import SocialMedia, Resume, Project, AdditionalInfo
from app.core.config import secret
class AnswerWithJustification(BaseModel):
            '''An answer to the user question along with justification for the answer.'''
            answer: str
            justification: str
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    google_api_key=secret.services.get("LLM").config.get("gemini"),
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract relevant information from the text. "
            "If you do not know the value of an attribute asked "
            "to extract, return null for the attribute's value.",
        ),
        
        ("human", "{text}"),
    ]
)
runnable = llm.with_structured_output(schema=AnswerWithJustification)
runnable_resume = prompt|llm.bind_tools([Resume])

# print(runnable.invoke({"text": 'Kolor Hijau Makan Daun Kelor'}))
print(runnable.invoke('Berapa 10 dikali 60?'))
print(runnable_resume.invoke({'text':'LinkedIn: https://www.linkedin.com/in/pradanaadn'}))