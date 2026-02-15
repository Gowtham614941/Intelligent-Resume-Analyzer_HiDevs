import re
from docx import Document
from PyPDF2 import PdfReader

def extract_text_from_pdf(path):
    try:
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def extract_text_from_docx(path):
    try:
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs)
    except Exception as e:
        print(f"Error reading DOCX: {e}")
        return ""

def parse_resume_text(text):
    # Improved Regex Patterns:
    # Name: Usually at the very top of the file
    name_match = re.search(r"^(?:Name[:\-]\s*)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)", text, re.M)
    
    # Email: Standard regex for email format
    email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    
    # Degree: Looks for keywords like Bachelor, Master, PhD, B.S., etc.
    degree_match = re.search(r"(Bachelor|Master|PhD|B\.S\.|M\.S\.|B\.A\.|Degree)[:\-]?\s*(.*)", text, re.I)
    
    # Experience: Looks for a number followed by 'year' or 'exp'
    exp_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:years?|yrs?)\s*(?:of\s*)?experience", text, re.I)
    # Fallback for your specific "Experience: 5" format
    if not exp_match:
        exp_match = re.search(r"Experience[:\-]\s*([\d\.]+)", text, re.I)

    # Skills: Looks for a 'Skills' header and captures until the next newline or section
    skills_match = re.search(r"Skills[:\-]\s*(.*)", text, re.I)

    return {
        "name": name_match.group(1).strip() if name_match else "Unknown",
        "email": email_match.group(0).strip() if email_match else "Unknown",
        "degree": degree_match.group(2).strip() if degree_match else "Unknown",
        "experience": float(exp_match.group(1)) if exp_match else 0.0,
        "skills": [s.strip().lower() for s in skills_match.group(1).split(",")] if skills_match else [],
    }

def parse_resume_file(path):
    path_lower = path.lower()
    if path_lower.endswith(".pdf"):
        text = extract_text_from_pdf(path)
    elif path_lower.endswith(".docx"):
        text = extract_text_from_docx(path)
    elif path_lower.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        raise ValueError(f"Unsupported file type: {path}")

    if not text.strip():
        print(f"Warning: No text could be extracted from {path}")
        return {"name": "Unknown", "email": "Unknown", "degree": "Unknown", "experience": 0, "skills": []}

    return parse_resume_text(text)
