"""Check whether a number is positive, negative or zero."""


def check_number(number: float) -> str:
    if number > 0:
        return f"{number} is Positive."
    elif number < 0:
        return f"{number} is Negative."
    else:
        return "Zero"


if __name__ == "__main__":
    try:
        number = float(input("Enter the number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        result = check_number(number=number)
        print(result)
