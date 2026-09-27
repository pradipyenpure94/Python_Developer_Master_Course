"""Count how many times a function is called."""


def function_call_count(func):
    """Count how many times a function call."""

    count = 0

    def wrapper(name: str):
        result = func(name)
        nonlocal count
        count += 1
        print(f"Call Count: {count}")
        return result
    return wrapper


@function_call_count
def greeting_message(name: str) -> None:
    """Simple a greeting message."""
    print(f"Hello {name}...!")


if __name__ == "__main__":
    greeting_message(name="Pradip")
    greeting_message(name="Pranali")
    greeting_message(name="Sanjay")
