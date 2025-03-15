RESUME_EXTRACTOR = (
    "You are an expert in extract markdown text to a python class or pydantic BaseModel\n"
    "Only extract relevant information from the {text}, that is a markdown from a resume\n"
    "If you do not know the value of an attribute asked to extract, return None for the attribute's value."
    "If there information about soft skill, technical skill, language proficiency pass it to Skill class"
    "Ensure the data is valid and you generate it from {text} with the same text/content, don't add data randomly."
    " If you don't know or can't parse, just return None "
)

