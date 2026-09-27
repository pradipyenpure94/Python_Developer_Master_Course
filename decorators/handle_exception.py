"""Handle exceptions using decorator."""


def handle_exception(func):
    """Create decorator that handle exceptions."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Error: {error}")
    return wrapper


@handle_exception
def division(
    first_number: int | float,
    second_number: int | float
) -> int | float:
    """Return the division of N input numbers."""
    return first_number / second_number


@handle_exception
def uppercase_name(name: str) -> str:
    """Return the uppercase name."""
    return name.upper()


if __name__ == "__main__":
    result = division(100, 4)
    print(f"Result: {result}")

    try:
        result = uppercase_name(name="Pradip")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Result: {result}")
