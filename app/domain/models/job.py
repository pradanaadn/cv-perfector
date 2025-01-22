from pydantic import BaseModel
from enum import Enum
from typing import Optional

        
class JobField(BaseModel):
    name:str
    descriptions:str
    
class EmploymentType(str, Enum):
    FULL_TIME = "Full-Time"
    PART_TIME = "Part-Time"
    TEMPORARY = "Temporary"
    CONTRACT = "Contract"
    FREELANCE = "Freelance"
    INTERNSHIP = "Internship"
    APPRENTICESHIP = "Apprenticeship"
    SEASONAL = "Seasonal"
    
class JobLevel(str, Enum):
    ENTRY_LEVEL = "Entry-Level"
    MID_LEVEL = "Mid-Level"
    SENIOR_LEVEL = "Senior-Level"
    EXECUTIVE_MANAGEMENT = "Executive/Management"
class JobDescriptions(BaseModel):
    description:str
    
class JobRequirements(BaseModel):
    requirements:str

class Company(BaseModel):
    name:str
    description:str
    industry:Optional[str]
    location:Optional[str]
    website:Optional[str]
    vision:Optional[str]
    mission:Optional[str]
    cultrue:Optional[str]

class Job(BaseModel):
    name:str
    field:JobField
    employment_type:EmploymentType
    level:JobLevel
    description:JobDescriptions
    requirements:JobRequirements
    company:Company