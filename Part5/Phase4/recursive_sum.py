"""Recursive sum from 1 to N."""


def recursive_sum(number: int) -> int:
    """Return the sum of 1 to N numbers."""
    if number < 0:
        raise ValueError("Number must be non-negative.")
    if number <= 1:
        return number
    return number + recursive_sum(number=number - 1)


if __name__ == "__main__":
    try:
        number = int(input("Enter the number: "))
        sum_of_n_numbers = recursive_sum(number=number)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Sum of 1 to {number} is: {sum_of_n_numbers}")
