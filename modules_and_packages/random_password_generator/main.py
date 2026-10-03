"""Random password generator."""

import secrets
import string


def random_password_generator(length: int = 8) -> str:
    """Return the random password."""
    if length < 8:
        raise ValueError("Password length must be at least 8.")
    characters = string.ascii_letters + string.punctuation + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


if __name__ == "__main__":
    try:
        password = random_password_generator()
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Password: {password}")
