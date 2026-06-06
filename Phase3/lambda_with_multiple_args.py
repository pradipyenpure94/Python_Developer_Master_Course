"""Lambda with multiple arguments."""


def addition(*args: int) -> int:
    """
    Return the sum of all arguments.

    Args:
        *args (int): Integer arguments

    Returns:
        int: Addition of each argument
    """
    add = lambda arguments: sum(arguments)
    return add(args)


if __name__ == "__main__":
    result = addition(10, 10, 20, 30)
    print(f"Addition: {result}")
