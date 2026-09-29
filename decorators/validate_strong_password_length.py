"""Validate strong password length."""

import string

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 10


def strong_password(func):
    """Create strong password."""
    def wrapper(password: str):

        if not MIN_PASSWORD_LENGTH <= len(password) <= MAX_PASSWORD_LENGTH:
            raise ValueError(
                "Password length must be between 8 and 10 characters."
            )

        digits = 0
        uppercase_letters = 0
        lowercase_letters = 0
        special_characters = 0

        for char in password:
            if char.isdigit():
                digits += 1
            elif char in string.ascii_uppercase:
                uppercase_letters += 1
            elif char in string.ascii_lowercase:
                lowercase_letters += 1
            elif char in string.punctuation:
                special_characters += 1

        if digits < 2:
            raise ValueError("Password must contain at least 2 digits.")
        if uppercase_letters < 2:
            raise ValueError(
                "Password must contain at least 2 uppercase characters."
            )
        if lowercase_letters < 2:
            raise ValueError(
                "Password must contain at least 2 lowercase characters."
            )
        if special_characters < 1:
            raise ValueError(
                "Password must contain at least 1 special character."
            )

        return func(password)
    return wrapper


@strong_password
def create_account(password: str):
    """Create new account."""
    print("Account created.")


if __name__ == "__main__":
    create_account(password="P2R_qi_3@_")
