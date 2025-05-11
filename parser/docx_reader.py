import docx

def read_docx(filepath: str) -> str:
    doc = docx.Document(filepath)
    return '\n'.join([para.text for para in doc.paragraphs])

