def generate_report(candidates, job):
    lines = []
    lines.append("=== Resume Analysis Report ===\n")

    lines.append(f"Job Title: {job['title']}")
    lines.append(f"Required Skills: {', '.join(job['skills'])}")
    lines.append(f"Required Degree: {job['degree']}")
    lines.append(f"Minimum Experience: {job['experience']} years\n")

    for i, c in enumerate(candidates, 1):
        status = (
            "Selected" if c.score >= 70 else "Maybe" if c.score >= 50 else "Rejected"
        )

        lines.append(f"Rank {i}: {c.name}")
        lines.append(f"Email: {c.email}")
        lines.append(f"Score: {c.score}")
        lines.append(f"Experience: {c.experience} years")
        lines.append(f"Degree: {c.degree}")
        lines.append(f"Decision: {status}")
        lines.append("-" * 40)

    return "\n".join(lines)