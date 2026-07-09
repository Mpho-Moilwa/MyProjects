class Applicant:

    def __init__(self, name, email, skills, experience):
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience
        self.score = 0

    def display(self):

        print("-" * 40)
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")
        print(f"Skills     : {', '.join(self.skills)}")
        print(f"Experience : {self.experience} years")
        print(f"Score      : {self.score}")
