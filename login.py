"""
=========================================
File: login.py
Author: Mpho Moilwa
=========================================
"""

# Default administrator account
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "Admin@123"


def login():
    """
    Authenticates the administrator.
    Allows a maximum of 3 login attempts.
    Returns True if successful, otherwise False.
    """

    print("=" * 50)
    print("      AI RESUME SCREENING SYSTEM")
    print("=" * 50)
    print("Administrator Login\n")

    attempts = 3

    while attempts > 0:

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("\n✅ Login successful.\n")
            return True

        attempts -= 1

        print(f"\n❌ Invalid username or password.")
        print(f"Remaining attempts: {attempts}\n")

    print("Too many failed login attempts.")
    print("Program terminated.")

    return False


def change_password():
    """
    Allows the administrator to change the password.
    (Temporary version - not yet saved to a file.)
    """

    global ADMIN_PASSWORD

    current = input("Enter current password: ")

    if current != ADMIN_PASSWORD:
        print("Incorrect current password.")
        return

    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new password: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    if len(new_password) < 8:
        print("Password must contain at least 8 characters.")
        return

    ADMIN_PASSWORD = new_password

    print("Password changed successfully.")
