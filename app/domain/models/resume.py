from typing import List, Optional, Union
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class Experience(BaseModel):
    company: str = Field(
        default=None,
        description="The name of the company or institution where the worker has experience in the resume.",
    )
    position: str = Field(
        default=None,
        description="The name of position where the worker has experience in the resume.",
    )
    start_date: datetime = Field(
        default=None,
        description="The start date where the worker has experience in the resume.",
    )
    end_date: Union[datetime, str] = Field(
        default=None,
        description="The end date of the worker's experience on the resume, or now if they are still working.",
    )
    description: Optional[str] = Field(
        default=None,
        description="he job description or accomplishment where the person has experience in the resume.",
    )


class Skill(BaseModel):
    name: str = Field(default=None, description="The skill of the person in the resume")
    level: Optional[str] = Field(
        default=None,
        description="The skill mastery or level of the person in the resume",
    )


class Education(BaseModel):
    institution: str = Field(
        default=None, description="The name of the educational institution."
    )
    degree: str = Field(default=None, description="The degree obtained or pursued.")
    start_date: str = Field(
        default=None, description="The start date of the education period."
    )
    end_date: Optional[str] = Field(
        default=None, description="The end date of the education period, if applicable."
    )
    description: Optional[str] = Field(
        default=None, description="The description of the education or course."
    )


class Project(BaseModel):
    name: str = Field(default=None, description="The name of the project.")
    project_link: Optional[str] = Field(
        default=None, description="The link to the project, if available."
    )
    start_date: Optional[str] = Field(
        default=None, description="The start date of the project."
    )
    end_date: Optional[str] = Field(
        default=None, description="The end date of the project, if applicable."
    )
    tech_stack: Optional[List[Skill]] = Field(
        default=None, description="The list of technologies used in the project."
    )
    description: Optional[str] = Field(
        default=None, description="A brief description of the project."
    )


class SocialMedia(BaseModel):
    name: str = Field(
        default=None,
        description="The name of the social media platform, git repository, or personal web.",
    )
    link: str = Field(
        default=None,
        description="The link to the social media platform, git repository, or personal web.",
    )
    username: Optional[str] = Field(
        default=None,
        description="The username or handle on the ssocial media platform, git repository, or personal web.",
    )


class AdditionalInfo(BaseModel):
    title: str = Field(
        default=None,
        description="The title or name of the additional information or section.",
    )
    start_date: Optional[str] = Field(
        default=None,
        description="The start date of the additional information or section.",
    )
    end_date: Optional[str] = Field(
        default=None,
        description="The end date of the additional informationor or section, if applicable.",
    )
    description: str = Field(
        default=None,
        description="The description or content of the additional information or section.",
    )


class Resume(BaseModel):
    name: str = Field(default=None, description="The name of the person in the resume")
    summary: str = Field(
        default=None, description="The summary of the person in the resume"
    )
    email: EmailStr = Field(
        default=None, description="The email of the person in the resume"
    )
    phone_number: str = Field(
        default=None, description="The phone number of the person in the resume"
    )
    address: str = Field(
        default=None, description="The address of the person in the resume"
    )
    social_media: List[SocialMedia] = Field(
        default=None,
        description="The list of social media profiles of the person in the resume",
    )
    education: List[Education] = Field(
        default=None, description="The list of education the person in the resume"
    )
    experiences: List[Experience] = Field(
        default=None, description="The list of experience the person in the resume"
    )
    skills: List[Skill] = Field(
        default=None, description="The list of skills the person in the resume"
    )
    projects: List[Project] = Field(
        default=None, description="The list of projects the person in the resume"
    )
    additional_info: Optional[List[AdditionalInfo]] = Field(
        default=None,
        description="The list of additional information the person in the resume",
    )
