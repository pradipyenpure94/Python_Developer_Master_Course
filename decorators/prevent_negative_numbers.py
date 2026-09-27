"""Prevent negative numbers."""


def positive_number(func):
    """Create decorator that validate positive number."""
    def wrapper(number: int):
        if number <= 0:
            raise ValueError("Positive number allowed only.")
        return func(number)
    return wrapper


@positive_number
def validate_positive_number(number: int):
    """Validate the positive number."""
    return number


if __name__ == "__main__":
    try:
        print(validate_positive_number(number=1))
    except ValueError as error:
        print(f"Error: {error}")
