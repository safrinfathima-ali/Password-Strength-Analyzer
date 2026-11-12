
import re
import secrets
import string
import getpass

common_passwords = [
    "password", "password123", "12345678",
    "123456789", "qwerty", "admin",
    "welcome", "iloveyou", "abc123"
]

def check_password(password):
    score = 0
    suggestions = []

    checks = {
        "At least 12 characters": len(password) >= 12,
        "Uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase letter": bool(re.search(r"[a-z]", password)),
        "Number": bool(re.search(r"[0-9]", password)),
        "Special character": bool(re.search(r"[^A-Za-z0-9]", password))
    }

    print("\n--- Password Security Analysis ---")

    for requirement, passed in checks.items():
        if passed:
            print("[+] " + requirement + ": Passed")
            score += 1
        else:
            print("[-] " + requirement + ": Failed")

    if len(password) < 12:
        suggestions.append("Use at least 12 characters.")

    if not checks["Uppercase letter"]:
        suggestions.append("Add uppercase letters.")

    if not checks["Lowercase letter"]:
        suggestions.append("Add lowercase letters.")

    if not checks["Number"]:
        suggestions.append("Include numbers.")

    if not checks["Special character"]:
        suggestions.append("Include special characters like @, #, !.")

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid commonly used passwords.")

    if re.search(r"(.)\1{3,}", password):
        score = max(0, score - 1)
        suggestions.append("Avoid repeating the same character.")

    if re.search(r"1234|2345|3456|abcd|qwer", password.lower()):
        score = max(0, score - 1)
        suggestions.append("Avoid predictable sequences.")

    if len(password) < 8 or password.lower() in common_passwords:
        strength = "Weak"
    elif score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print("\nPassword Strength:", strength)
    print("Security Score:", str(score) + "/5")

    if suggestions:
        print("\nSuggestions to improve your password:")
        for tip in suggestions:
            print("- " + tip)
    else:
        print("\nExcellent! Your password passed all basic checks.")

def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*")
    ]

    password += [secrets.choice(characters) for _ in range(12)]

    secrets.SystemRandom().shuffle(password)

    return "".join(password)

def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    while True:
        print("\n1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            password = getpass.getpass("Enter your password: ")

            if not password:
                print("Please enter a password.")
            else:
                check_password(password)

        elif choice == "2":
            new_password = generate_password()
            print("\nGenerated Strong Password:", new_password)
            print("Store it securely and do not share it.")

        elif choice == "3":
            print("\nThank you for using Password Strength Analyzer!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
