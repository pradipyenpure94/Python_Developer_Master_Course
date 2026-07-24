"""Validate email."""

from replace_substring import validate_text


def validate_email(email: str) -> bool:
    """
    Check whether the email is valid.

    Args:
        email (str): User input email.

    Returns:
        bool: True if the email is valid, otherwise False.
    """
    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    local_part, domain_part = email.split("@")
    if (not local_part or
        not domain_part or
        domain_part.count(".") != 1
    ):
        return False
    if domain_part.startswith(".") or domain_part.endswith("."):
        return False

    return True


def main() -> None:
    """Run the Main Program."""
    try:
        email = input("Enter the email: ").strip()
        validate_text(value=email, field_name="Email")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if validate_email(email=email):
            print(f"{email} is a valid email address.")
        else:
            print(f"{email} is not a valid email address.")


if __name__ == "__main__":
    main()
