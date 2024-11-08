from pymupdf4llm import to_markdown
from markdown_to_json import dictify, jsonify

def cv2md(file_path:str)->str:
    """Function to convert CV in PDF to Markdown
    Args:
        file_path (str):file path of the CV

    Returns:
        str: CV in Markdown Format
    """
    
    md = to_markdown(file_path)
    print(md)
    return md


print(jsonify(cv2md(file_path='CV_AI_PRADANA.pdf')))