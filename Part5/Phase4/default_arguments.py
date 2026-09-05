"""Function with default arguments."""


def hello_greetings(name: str = "world") -> str:
    """Name greetings."""
    return f"Hello {name}...!"


if __name__ == "__main__":
    result = hello_greetings(name="Sanjay")
    print(result)
