"""Login validation."""

from getpass import getpass

MAX_PASSWORD_ATTEMPTS = 3
USERNAME = "admin"
PASSWORD = "Admin123@"


def validate_username(username: str) -> None:
    """Validate the username."""
    if not username:
        raise ValueError("Username cannot be empty.")
    if username != USERNAME:
        raise ValueError("Invalid username. Please enter a valid username.")


def verify_password(stored_password: str) -> bool:
    """Verify the user's password and authenticate them."""
    attempts = 0

    while attempts < MAX_PASSWORD_ATTEMPTS:
        password = getpass("Enter the password: ")

        if not password:
            print("Password cannot be empty.")
            continue

        if password != stored_password:
            attempts += 1

            if attempts == MAX_PASSWORD_ATTEMPTS:
                print("Account Locked.")
                return False
            print(
                "Invalid password. Remaining attempts: "
                f"{MAX_PASSWORD_ATTEMPTS - attempts}")
            continue

        print("Login successful.")
        return True


def main() -> None:
    """Run the Program."""
    try:
        user_name = input("Enter the username: ").strip()
        validate_username(username=user_name)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if verify_password(PASSWORD):
            print(f"Welcome, {user_name}.")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
