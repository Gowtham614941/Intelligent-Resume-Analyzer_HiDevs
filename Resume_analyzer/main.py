from utils import (
    get_non_empty,
    get_valid_email,
    get_valid_number,
    get_valid_skills,
    get_valid_int,
)
from models import Candidate
from matcher import rank_candidates
from reporter import generate_report
from file_manager import save_results
from parser import parse_resume_file, parse_resume_text


def load_job():
    print("\n=== Enter Job Details ===")
    title = get_non_empty("Job Title: ")
    skills = get_valid_skills("Required Skills (comma separated): ")
    experience = get_valid_number("Minimum Experience (years): ", 0, 50)
    degree = get_non_empty("Required Degree: ")

    return {
        "title": title,
        "skills": skills,
        "experience": experience,
        "degree": degree,
    }
    


def load_candidate():
    print("\nResume Input Type:")
    print("1 → Manual Resume Entry")
    print("2 → Upload Resume File (PDF/DOCX/TXT)")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        # ... (manual entry logic) ...
        data = parse_resume_text(text)
    elif choice == "2":
        path = get_non_empty("Enter resume file path: ")
        data = parse_resume_file(path)
    else:
        print("Invalid choice. Try again.")
        return load_candidate()

    # SAFE EXTRACTION: Use .get() to provide defaults if keys are missing
    return Candidate(
        name=data.get("name", "Unknown"),
        email=data.get("email", "Unknown"),
        skills=data.get("skills", []),
        experience=data.get("experience", 0.0),
        degree=data.get("degree", "Unknown"))

    else:
        print("Invalid choice. Try again.")
        return load_candidate()

    return Candidate(
    data["name"],
    data["email"],
    data["skills"],
    data["experience"],
    data["degree"]
    )


def main():
    print("=== Intelligent Resume Analyzer ===")

    job = load_job()
    n = get_valid_int("\nNumber of candidates: ", 1, 100)

    candidates = []
    for _ in range(n):
        candidates.append(load_candidate())

    ranked = rank_candidates(candidates, job)

    report = generate_report(ranked, job)
    print("\n" + report)

    save_results(ranked, job)
    print("\nResults saved to results.json")


if __name__ == "__main__":

    main()
