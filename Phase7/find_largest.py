"""Find the largest of three numbers without using max()."""


def find_largest_number(
    first_number: float,
    second_number: float,
    third_number: float
) -> float:
    if first_number >= second_number >= third_number:
        return first_number
    elif second_number >= third_number >= first_number:
        return second_number
    else:
        return third_number


if __name__ == "__main__":
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        third_number = float(input("Enter the third number: "))
    except ValueError as error:
        print(f"Error: {error}")
    else:
        largest_number = find_largest_number(
            first_number=first_number,
            second_number=second_number,
            third_number=third_number
        )
        print(f"Largest number: {largest_number}")
