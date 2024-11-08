import pymupdf4llm
import pathlib

md_text = pymupdf4llm.to_markdown("CV_AI_PRADANA.pdf")

pathlib.Path("output.md").write_bytes(md_text.encode())