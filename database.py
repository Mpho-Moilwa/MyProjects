applicants = []


def add_applicant(applicant):
    applicants.append(applicant)


def show_applicants():

    if len(applicants) == 0:
        print("\nNo applicants found.\n")
        return

    for applicant in applicants:
        applicant.display()


def search(name):

    for applicant in applicants:

        if applicant.name.lower() == name.lower():
            return applicant

    return None


def rank():

    applicants.sort(
        key=lambda applicant: applicant.score,
        reverse=True
    )

    print("\nTOP APPLICANTS\n")

    for applicant in applicants:
        print(f"{applicant.name:<20} {applicant.score}")
