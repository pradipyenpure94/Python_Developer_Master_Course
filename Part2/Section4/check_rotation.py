"""Check rotation."""

from collections import deque
from reverse_string import validate_string


def is_rotation(first_string: str, second_string: str) -> bool:
    """
    Check whether one string is a rotation of the other.

    Args:
        first_string (str): First input string.
        second_string (str): Second input string.

    Returns:
        bool: True if one string is a rotation of the other, otherwise False.
    """
    if len(first_string) != len(second_string):
        return False

    first_deque = deque(first_string)
    second_deque = deque(second_string)

    if first_deque == second_deque:
        return True

    for _ in range(len(first_string) - 1):
        first_deque.rotate(1)
        if first_deque == second_deque:
            return True

    return False


def main() -> None:
    """Run the Main Program."""
    try:
        first_string = input("Enter the first string: ").strip()
        validate_string(input_string=first_string)
        second_string = input("Enter the second string: ").strip()
        validate_string(input_string=second_string)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if is_rotation(first_string=first_string, second_string=second_string):
            print("The strings are rotations of each other.")
        else:
            print("The strings are not rotations of each other.")


if __name__ == "__main__":
    main()
