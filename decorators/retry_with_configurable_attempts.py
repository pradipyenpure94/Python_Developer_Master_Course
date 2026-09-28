"""Retry with configurable attempts."""


def retry(max_attempts):
    """Retry with configurable attempts."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempts: {attempt + 1}: {e}")
            raise Exception("Maximum attempts exceeded.")
        return wrapper
    return decorator


@retry(max_attempts=3)
def division(first_number: float, second_number: float) -> float:
    """Return the division of two numbers."""
    return first_number / second_number


if __name__ == "__main__":
    print(division(first_number=10, second_number=2))
