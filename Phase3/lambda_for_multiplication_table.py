"""Lambda for multiplication table."""


def multiplication_table(num: int) -> list[int]:
    """
    Return the multiplication table list.

    Args:
        num (int): Input number.

    Returns:
        list[int]: Multiplication table of list.
    """
    table = lambda n: [n * i for i in range(1, 11)]
    return table(num)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = multiplication_table(num=number)
        print(f"Multiplication table of {number} is: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
