"""
=========================================
File: main.py
Author: Mpho Moilwa
=========================================
"""

from applicant import Applicant
from screening import calculate_score
from database import *
from login import login


# ----------------------------
# Start Program
# ----------------------------

if not login():
    exit()

load()


# ----------------------------
# Main Menu
# ----------------------------

while True:

    print("\n" + "=" * 55)
    print("        AI RESUME SCREENING SYSTEM")
    print("=" * 55)

    print("1. Register Applicant")
    print("2. View Applicants")
    print("3. Search Applicant")
    print("4. Rank Applicants")
    print("5. Delete Applicant")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    # ---------------------------------
    # Register Applicant
    # ---------------------------------

    if choice == "1":

        applicant_id = len(applicants) + 1001

        name = input("First Name: ")

        surname = input("Surname: ")

        email = input("Email: ")

        phone = input("Phone Number: ")

        skills = input(
            "Skills (comma separated): "
        ).split(",")

        skills = [skill.strip() for skill in skills]

        experience = int(
            input("Years of Experience: ")
        )

        education = input(
            "Education (Bachelors/Honours/Masters): "
        )

        applicant = Applicant(
            applicant_id,
            name,
            surname,
            email,
            phone,
            skills,
            experience,
            education
        )

        calculate_score(applicant)

        applicant.score += applicant.calculate_bonus()

        if applicant.score > 100:
            applicant.score = 100

        applicant.update_status()

        add_applicant(applicant)

        print("\nApplicant registered successfully!")

    # ---------------------------------
    # View Applicants
    # ---------------------------------

    elif choice == "2":

        show_applicants()

    # ---------------------------------
    # Search Applicant
    # ---------------------------------

    elif choice == "3":

        name = input("Enter applicant name: ")

        applicant = search(name)

        if applicant:
            applicant.display()
        else:
            print("\nApplicant not found.")

    # ---------------------------------
    # Rank Applicants
    # ---------------------------------

    elif choice == "4":

        rank()

    # ---------------------------------
    # Delete Applicant
    # ---------------------------------

    elif choice == "5":

        name = input("Applicant name to delete: ")

        if delete(name):
            print("Applicant deleted successfully.")
        else:
            print("Applicant not found.")

    # ---------------------------------
    # Exit
    # ---------------------------------

    elif choice == "6":

        save()

        print("\nThank you for using the system.")

        print("Goodbye!")

        break

    else:

        print("\nInvalid option.")
