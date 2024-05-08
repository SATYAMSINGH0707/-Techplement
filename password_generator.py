import random
import string
import argparse

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
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
    parser.add_argument("--no-uppercase", dest="uppercase", action="store_false", help="Exclude uppercase letters")
    parser.add_argument("--no-lowercase", dest="lowercase", action="store_false", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", dest="digits", action="store_false", help="Exclude digits")
    parser.add_argument("--no-special-chars", dest="special_chars", action="store_false", help="Exclude special characters")
    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special_chars)
        print("Generated password:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
