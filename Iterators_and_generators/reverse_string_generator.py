"""Reverse String Generator."""


from collections.abc import Generator


def generate_reverse_string(text: str) -> Generator[str]:
    """Generate the reverse string."""
    for i in range(len(text) - 1, -1, -1):
        yield text[i]


if __name__ == "__main__":
    string = generate_reverse_string(text="Pradip")

    print(next(string))
    print(next(string))
    print(next(string))
    print("In for loop")
    for char in string:
        print(char)
