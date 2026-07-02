"""
Buid a Login System Using exception handling.

Requirements:
    1. Username.
    2. Password.
    3. Three attempts.
    4. Raise custom exception on failure.
"""


class InvalidCredentialsException(Exception):
    """Raised when the username or password is invalid."""


VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"
MAX_ATTEMPTS = 3


def login(username: str, password: str) -> None:
    """
    Validate the user's login credentials.

    Args:
        username (str): Input username.
        password (str): Input password.

    Raises:
        InvalidCredentialsException: If the username or password is incorrect.
    """
    if username != VALID_USERNAME or password != VALID_PASSWORD:
        raise InvalidCredentialsException("Invalid username or password.")


def main() -> None:
    """Run the login system."""

    attempts = MAX_ATTEMPTS

    while attempts > 0:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")

            login(username=username, password=password)

        except InvalidCredentialsException as error:
            attempts -= 1
            print(f"Error: {error}")
            if attempts > 0:
                print(f"Attempts remaining: {attempts}")
            else:
                print("Maximum login attempts exceeded.")

        else:
            print("Login successful!")
            break
        finally:
            print("Operation completed.")
            print("-" * 30)


if __name__ == "__main__":
    main()
