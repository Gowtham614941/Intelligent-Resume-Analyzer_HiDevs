def calculate_score(candidate, job):
    score = 0
    
    # Identify matches and gaps
    job_skills_set = set(job["skills"])
    candidate_skills_set = set(candidate.skills)
    
    matched_skills = job_skills_set & candidate_skills_set
    # New logic: Identify what is missing
    candidate.missing_skills = list(job_skills_set - candidate_skills_set)
    
    score += len(matched_skills) * 10
    score += candidate.experience * 5

    if candidate.degree == job["degree"].lower():
        score += 20

    if candidate.experience >= job["experience"]:
        score += 15

    candidate.score = round(score, 2)
    return candidate.score


def rank_candidates(candidates, job):
    for c in candidates:
        calculate_score(c, job)


    return sorted(candidates, key=lambda x: x.score, reverse=True)

