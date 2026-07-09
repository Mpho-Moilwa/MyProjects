import random
import string


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=" * 35)
    print("     PASSWORD GENERATOR")
    print("=" * 35)

    length = int(input("Enter password length: "))

    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
