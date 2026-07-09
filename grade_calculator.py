# -----------------------------------------
# Student Grade Calculator
# Author: Mpho Moilwa
# -----------------------------------------

def calculate_average(marks):
    return sum(marks) / len(marks)


def get_grade(average):
    if average >= 75:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def main():
    print("=" * 40)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 40)

    student_name = input("Enter student name: ")

    marks = []

    number_of_subjects = int(input("How many subjects? "))

    for i in range(number_of_subjects):
        while True:
            try:
                mark = float(input(f"Enter mark {i + 1}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    average = calculate_average(marks)
    grade = get_grade(average)

    print("\nRESULTS")
    print("-" * 30)
    print("Student:", student_name)
    print("Average:", round(average, 2))
    print("Final Grade:", grade)


if __name__ == "__main__":
    main()
