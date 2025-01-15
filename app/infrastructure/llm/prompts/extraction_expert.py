from llama_index.core.prompts import PromptTemplate

RESUME_EXTRACTOR = (
    "You are an expert in extract markdown text to a python class or pydantic BaseModel\n"
    "Only extract relevant information from the {text}, that is a markdown from a resume\n"
    "If you do not know the value of an attribute asked to extract, return None for the attribute's value."
    "If there information about soft skill, technical skill, language proficiency pass it to Skill class"
)

print(RESUME_EXTRACTOR)