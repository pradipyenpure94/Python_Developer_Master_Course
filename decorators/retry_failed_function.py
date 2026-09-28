"""Retry failed function."""


def retry(func):
    """Create decorator that retry failed function."""
    def wrapper(*args, **kwargs):
        for attempt in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempts: {attempt + 1}")
                print(f"Error: {e}")
        raise Exception("Function failed after 3 attempts.")
    return wrapper


@retry
def division(first_number, second_number):
    """Return the division of two numbers."""
    return first_number / second_number


if __name__ == "__main__":
    print(division(first_number=10, second_number=0))
