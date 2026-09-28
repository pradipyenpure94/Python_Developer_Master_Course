"""Validate email."""


def validate_email(func):
    """Create decorator of validate email."""
    def wrapper(email: str):
        if "@" not in email:
            raise ValueError("Invalid email.")
        local_part, domain_part = email.split("@", 1)
        if not local_part:
            raise ValueError("Email user name is required.")
        if not domain_part:
            raise ValueError("Email domain is required.")
        if "." not in domain_part:
            raise ValueError("Invalid email domain.")
        return func(email)
    return wrapper


@validate_email
def register_email(email: str):
    print("Successfully registered.")


if __name__ == "__main__":
    register_email(email="pradipgmail.com")
