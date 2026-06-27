"""Print multiplication table of a number."""


def print_multiplication_table(num: int) -> None:
    """
    Print multiplication table of a number.

    Args:
        num (int): Input number.

    Returns:
        None.
    """
    print(f"Multiplication table of {num} is:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        print_multiplication_table(num=number)
    finally:
        print("Operation completed.")
