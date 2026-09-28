"""Validate email."""


def validate_email(func):
    """Create decorator of validate email."""
    def wrapper(email: str):
        if "@" not in email:
            raise ValueError("Invalid email.")
        return func(email)
    return wrapper


@validate_email
def register_email(email: str):
    print("Successfully registered.")


if __name__ == "__main__":
    register_email(email="pradip@gmail.com")
