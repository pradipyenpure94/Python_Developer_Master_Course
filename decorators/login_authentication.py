"""Login authentication decorator."""


login = True


def login_authentication(func):
    """Create decorator that login authentication."""
    def wrapper(*args, **kwargs):
        if not login:
            return "Please login first."
        return func(*args, **kwargs)
    return wrapper


@login_authentication
def division(first_number: float, second_number: float) -> float:
    """Return the division of two numbers."""
    return first_number / second_number


if __name__ == "__main__":
    result = division(first_number=10, second_number=2)
    print(result)
