import re
from docx import Document
from PyPDF2 import PdfReader


def extract_text_from_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)


def parse_resume_text(text):
    name = re.search(r"Name[:\-]\s*(.*)", text, re.I)
    email = re.search(r"Email[:\-]\s*(.*)", text, re.I)
    degree = re.search(r"Degree[:\-]\s*(.*)", text, re.I)
    exp = re.search(r"Experience[:\-]\s*([\d\.]+)", text, re.I)
    skills = re.search(r"Skills[:\-]\s*(.*)", text, re.I)

    return {
        "name": name.group(1).strip() if name else "Unknown",
        "email": email.group(1).strip() if email else "Unknown",
        "degree": degree.group(1).strip() if degree else "Unknown",
        "experience": float(exp.group(1)) if exp else 0,
        "skills": [s.strip().lower() for s in skills.group(1).split(",")] if skills else [],
    }


def parse_resume_file(path):
    if path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(path)
    elif path.lower().endswith(".docx"):
        text = extract_text_from_docx(path)
    elif path.lower().endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        raise ValueError("Unsupported file type")

    return parse_resume_text(text)