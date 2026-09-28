"""Return default value when exception occurs."""


def safe_execute(default_value):
    """Return default value when exception occurs."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                return default_value
        return wrapper
    return decorator


@safe_execute(0)
def division(first_number: float, second_number: float) -> float:
    """Return the division of two numbers."""
    return first_number / second_number


if __name__ == "__main__":
    print(division(first_number=10, second_number=4))
