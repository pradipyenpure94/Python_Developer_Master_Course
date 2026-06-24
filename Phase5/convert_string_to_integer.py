"""Convert string to integer."""


def convert_string_to_integer(num: str) -> int:
    """
    Convert number string to integer value.

    Args:
        num (str): Input number.

    Returns:
        int: Converted integer value.
    """
    return int(num)


if __name__ == "__main__":
    try:
        number = input("Enter a number: ")
        result = convert_string_to_integer(num=number)
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        print(f"Result: {result}")
    finally:
        print("Operation completed.")
