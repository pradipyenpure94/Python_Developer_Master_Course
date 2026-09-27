"""Validate string arguments."""


def validate_string_arguments(func):
    """Create decorator that validate a string."""

    def wrapper(name: str):
        if not isinstance(name, str):
            raise TypeError("Argument must be a string.")
        return func(name)
    return wrapper


@validate_string_arguments
def uppercase_name(name: str) -> str:
    """Return the uppercase string."""
    return name.upper()


if __name__ == "__main__":
    try:
        print(uppercase_name(name="Pradip"))
    except TypeError as error:
        print(f"Error: {error}")
