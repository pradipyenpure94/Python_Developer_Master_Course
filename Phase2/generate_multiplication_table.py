"""Generate multiplication table."""


def generate_multiplication_table(num: int) -> None:
    """
    Display the multiplication table of input number.

    Args:
        num (int): Input number.

    Returns:
        None
    """
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        print(f"Multiplication table of {number} is:")
        generate_multiplication_table(num=number)
    except ValueError as error:
        print(f"{error}")
