import re


def get_non_empty(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Invalid input.")


def get_valid_email(prompt):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    while True:
        email = input(prompt)
        if re.match(pattern, email):
            return email
        print("Invalid email format.")


def get_valid_number(prompt, min_val=0, max_val=100):
    while True:
        try:
            num = float(input(prompt))
            if min_val <= num <= max_val:
                return num
        except:
            pass
        print("Invalid number.")


def get_valid_int(prompt, min_val=1, max_val=100):
    while True:
        try:
            num = int(input(prompt))
            if min_val <= num <= max_val:
                return num
        except:
            pass
        print("Invalid integer.")


def get_valid_skills(prompt):
    while True:
        skills = input(prompt)
        if skills.strip():
            return [s.strip().lower() for s in skills.split(",")]
        print("Skills cannot be empty.")