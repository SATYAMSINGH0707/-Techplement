import random
import string
import argparse

def generate_password(length, uppercase, lowercase, digits, special_chars):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one type of character (uppercase, lowercase, digit, special character) must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("length", type=int, help="Length of the password (required)")
    parser.add_argument("--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("--lowercase", action="store_true", help="Include lowercase letters")
    parser.add_argument("--digits", action="store_true", help="Include digits")
    parser.add_argument("--special-chars", action="store_true", help="Include special characters")
    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special_chars)
        print("Generated password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
