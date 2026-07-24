"""Validate password."""

from string import punctuation
from replace_substring import validate_text

PASSWORD_LENGTH_LIMIT = 8
UPPERCASE_LETTER_LIMIT = 2
LOWERCASE_LETTER_LIMIT = 1
DIGIT_LIMIT = 1
SPECIAL_CHARACTER_LIMIT = 1


def validate_password(password: str) -> None:
    """
    Check whether the password is valid.

    Args:
        password (str): User input password.

    Raises:
        ValueError: If the password does not satisfy the business rules.
    """
    if len(password) != PASSWORD_LENGTH_LIMIT:
        raise ValueError(
            "Password length must be exactly "
            f"{PASSWORD_LENGTH_LIMIT} characters."
        )
    if " " in password:
        raise ValueError("Password cannot contain spaces.")
    if sum(1 for char in password if char.isupper()) < UPPERCASE_LETTER_LIMIT:
        raise ValueError(
            f"Password must contain at least {UPPERCASE_LETTER_LIMIT} "
            "uppercase letter(s).")
    if sum(1 for char in password if char.islower()) < LOWERCASE_LETTER_LIMIT:
        raise ValueError(
            f"Password must contain at least {LOWERCASE_LETTER_LIMIT} "
            "lowercase letter(s).")
    if sum(char.isdigit() for char in password) < DIGIT_LIMIT:
        raise ValueError(
            f"Password must contain at least {DIGIT_LIMIT} digit(s)."
        )
    if sum(
        1 for char in password if char in punctuation
    ) < SPECIAL_CHARACTER_LIMIT:
        raise ValueError(
            f"Password must contain at least {SPECIAL_CHARACTER_LIMIT} "
            "special character(s).")


def main() -> None:
    """Run the Main Program."""
    try:
        password = input("Enter the password: ").strip()
        validate_text(value=password, field_name="Password")
        validate_password(password=password)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print("Password is valid.")


if __name__ == "__main__":
    main()
