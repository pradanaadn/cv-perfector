from typing import List, Optional, Union
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class Experience(BaseModel):
    """
    Experience model representing a worker's job experience.

    Attributes:
        company (str): The name of the company or institution where the worker has experience in the resume.
        position (str): The name of the position where the worker has experience in the resume.
        start_date (Union[datetime, str, None]): The start date of the worker's experience in the resume.
        end_date (Union[datetime, str, None]): The end date of the worker's experience in the resume, or now if they are still working.
        description (Optional[str]): The job description or accomplishment where the person has experience in the resume.
    """

    company: str = Field(
        default=None,
        description="The name of the company or institution where the worker has experience in the resume.",
    )
    position: str = Field(
        default=None,
        description="The name of position where the worker has experience in the resume.",
    )
    start_date: Union[datetime, str, None] = Field(
        default=None,
        description="The start date where the worker has experience in the resume.",
    )
    end_date: Union[datetime, str, None] = Field(
        default=None,
        description="The end date of the worker's experience on the resume, or now if they are still working.",
    )
    description: Optional[str] = Field(
        default=None,
        description="he job description or accomplishment where the person has experience in the resume.",
    )


class Skill(BaseModel):
    """
    Represents a skill in a resume.

    Attributes:
        name (str): The skill of the person in the resume.
        level (Optional[str]): The skill mastery or level of the person in the resume.
    """

    name: str = Field(default=None, description="The skill of the person in the resume")
    level: Optional[str] = Field(
        default=None,
        description="The skill mastery or level of the person in the resume",
    )


class Certification(BaseModel):
    name: str = Field(default=None, description="The skill of the person in the resume")
    link: Optional[str] = Field(
        default=None,
        description="The link to the certification, if available.",
    )
    start_date: Union[datetime, str, None] = Field(
        default=None, description="The start date of the certification, if applicable."
    )
    expired_date: Union[datetime, str, None] = Field(
        default=None, description="The end date of the certification, if applicable."
    )
    description: Optional[str] = Field(
        default=None,
        description="The skill mastery or level of the person in the resume",
    )


class Education(BaseModel):
    """
    Represents an educational qualification or period of study.

    Attributes:
        institution (str): The name of the educational institution.
        degree (str): The degree obtained or pursued.
        start_date (Union[datetime, str, None]): The start date of the education period.
        end_date (Union[datetime, str, None]): The end date of the education period, if applicable.
        description (Optional[str]): The description of the education or course.
    """

    institution: str = Field(
        default=None, description="The name of the educational institution."
    )
    degree: str = Field(default=None, description="The degree obtained or pursued.")
    start_date: Union[datetime, str, None] = Field(
        default=None, description="The start date of the education period."
    )
    end_date: Union[datetime, str, None] = Field(
        default=None, description="The end date of the education period, if applicable."
    )
    description: Optional[str] = Field(
        default=None, description="The description of the education or course."
    )


class Project(BaseModel):
    """
    Represents a project in a resume.

    Attributes:
        name (str): The name of the project.
        project_link (Optional[str]): The link to the project, if available.
        start_date (Union[datetime, str, None]): The start date of the project.
        end_date (Union[datetime, str, None]): The end date of the project, if applicable.
        tech_stack (Optional[List[Skill]]): The list of technologies used in the project.
        description (Optional[str]): A brief description of the project.
    """

    name: str = Field(default=None, description="The name of the project.")
    project_link: Optional[str] = Field(
        default=None, description="The link to the project, if available."
    )
    start_date: Union[datetime, str, None] = Field(
        default=None, description="The start date of the project."
    )
    end_date: Union[datetime, str, None] = Field(
        default=None, description="The end date of the project, if applicable."
    )
    tech_stack: Optional[List[Skill]] = Field(
        default=None, description="The list of technologies used in the project."
    )
    description: Optional[str] = Field(
        default=None, description="A brief description of the project."
    )


class SocialMedia(BaseModel):
    """
    SocialMedia model representing a user's social media profile.

    Attributes:
        name (str): The name of the social media platform, git repository, or personal web.
        link (str): The link to the social media platform, git repository, or personal web.
        username (Optional[str]): The username or handle on the social media platform, git repository, or personal web.
    """

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
    """
    AdditionalInfo model to represent additional information or activities in a resume.

    Attributes:
        name (str): The name of the additional information or activity.
        start_date (Union[datetime, str, None]): The start date of the additional information or activity.
        end_date (Union[datetime, str, None]): The end date of the additional information or activity, if applicable.
        description (str): The description or content of the additional information or activity.
    """

    name: str = Field(
        default=None,
        description="The name the additional information or activity.",
    )
    start_date: Union[datetime, str, None] = Field(
        default=None,
        description="The start date of the additional information or activity.",
    )
    end_date: Union[datetime, str, None] = Field(
        default=None,
        description="The end date of the additional informationor or activity, if applicable.",
    )
    description: str = Field(
        default=None,
        description="The description or content of the additional information or activity.",
    )


class AdditionalSection(BaseModel):
    """
    AdditionalSection represents an additional section in a resume.
    Attributes:
        title (str): The title of the additional section in the resume.
        additional_info (Optional[List[AdditionalInfo]]): The list of additional info in the resume.
    """

    title: str = Field(
        default=None,
        description="The title the additional section in the resume.",
    )
    additional_info: Optional[List[AdditionalInfo]] = Field(
        default=None, description="The list of additional info in the resume"
    )


class Resume(BaseModel):
    """
    Resume model representing a person's resume details.

    Attributes:
        name (Optional[str]): The name of the person in the resume.
        summary (Optional[str]): The summary of the person in the resume.
        email (Optional[EmailStr]): The email of the person in the resume.
        phone_number (Optional[str]): The phone number of the person in the resume.
        address (Optional[str]): The address of the person in the resume.
        social_media (Optional[List[SocialMedia]]): The list of social media profiles of the person in the resume.
        education (Optional[List[Education]]): The list of education the person in the resume.
        experiences (Optional[List[Experience]]): The list of experience the person in the resume.
        skills (Optional[List[Skill]]): The list of skills the person in the resume.
        certification (Optional[List[Certification]]): The list of certifications the person in the resume.
        projects (Optional[List[Project]]): The list of projects the person in the resume.
        additional_section (Optional[List[AdditionalSection]]): The list of additional sections the person in the resume.
    """

    name: Optional[str] = Field(
        default=None, description="The name of the person in the resume"
    )
    summary: Optional[str] = Field(
        default=None, description="The summary of the person in the resume"
    )
    email: Optional[EmailStr] = Field(
        default=None, description="The email of the person in the resume"
    )
    phone_number: Optional[str] = Field(
        default=None, description="The phone number of the person in the resume"
    )
    address: Optional[str] = Field(
        default=None, description="The address of the person in the resume"
    )
    social_media: Optional[List[SocialMedia]] = Field(
        default=None,
        description="The list of social media profiles of the person in the resume",
    )
    education: Optional[List[Education]] = Field(
        default=None, description="The list of education the person in the resume"
    )
    experiences: Optional[List[Experience]] = Field(
        default=None, description="The list of experience the person in the resume"
    )
    skills: Optional[List[Skill]] = Field(
        default=None, description="The list of skills the person in the resume"
    )
    certification: Optional[List[Certification]] = Field(
        default=None, description="The list of certifications the person in the resume"
    )
    projects: Optional[List[Project]] = Field(
        default=None, description="The list of projects the person in the resume"
    )
    additional_section: Optional[List[AdditionalSection]] = Field(
        default=None,
        description="The list of additional section the person in the resume",
    )
