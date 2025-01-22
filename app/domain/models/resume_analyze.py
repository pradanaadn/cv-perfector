from pydantic import BaseModel


class Analysis(BaseModel):
    section_name: str
    overview: str
    improvements_needed: str
    strengths: str
    recommended_actions: str
    score: float
    
    