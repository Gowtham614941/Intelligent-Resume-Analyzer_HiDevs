class Candidate:
    def __init__(self, name, email, skills, experience, degree):
        self.name = name
        self.email = email
        # Ensure skills is always a list even if parser returns None
        self.skills = [s.lower() for s in skills] if skills else [] 
        self.experience = float(experience) if experience else 0.0
        # Normalize degree to lowercase immediately
        self.degree = str(degree).lower().strip() if degree else "unknown"
        self.score = 0

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "skills": self.skills,
            "experience": self.experience,
            "degree": self.degree,
            "score": self.score,

        }
