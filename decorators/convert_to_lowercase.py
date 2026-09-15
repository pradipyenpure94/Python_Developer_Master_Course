"""Decorator That Converts Result To Lowercase."""


def lowercase(func):
    """Simple lowercase decorator."""
    def lowercase_extend(*args, **kwargs):
        """To extend the lowercase decorator."""
        result = func(*args, **kwargs)
        return result.lower()
    return lowercase_extend


@lowercase
def to_lower(text):
    """To convert the lowercase text."""
    return text


if __name__ == "__main__":
    result = to_lower(text="MIT Pune")
    print(result)
