"""Convert string input into the correct numeric type with validation."""

number = input("Enter the number: ")


def convert_to_number(number: str) -> int | float:
    number = number.strip()
    if not number:
        raise ValueError("Number cannot be empty.")
    try:
        return int(number)
    except ValueError:
        try:
            return float(number)
        except ValueError:
            raise ValueError(
                f"Cannot convert '{number}' to a valid numeric type."
            ) from None


result = convert_to_number(number=number)
print(f"Number: {result}")
