class Candidate:
    def __init__(self, name, email, skills, experience, degree):
        self.name = name
        self.email = email
        self.skills = [s.lower() for s in skills]
        self.experience = experience
        self.degree = degree.lower()
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