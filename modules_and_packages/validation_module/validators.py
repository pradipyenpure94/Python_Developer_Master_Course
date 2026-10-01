"""Validation / Business Rules."""


def is_positive(number: int) -> bool:
    """Return True if the number is positive otherwise False."""
    return number > 0


def is_valid_email(email: str) -> bool:
    """Validate the email address format."""
    if "@" not in email:
        raise ValueError("Invalid email.")
    local_part, domain_part = email.split("@", 1)
    if not local_part:
        raise ValueError("User name is required.")
    if not domain_part:
        raise ValueError("Domain is required.")
    if "." not in domain_part:
        raise ValueError("Domain must contain a dot.")
    if "@" in domain_part:
        raise ValueError("Invalid email.")

    return True
