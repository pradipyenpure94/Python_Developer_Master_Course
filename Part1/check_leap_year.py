"""Check whether a year is a leap year."""


def is_leap_year(year: int) -> bool:
    """
    Check whether a year is a leap year.

    Args:
        year (int): Input year.

    Returns:
        bool: True if the year is a leap year, otherwise False.
    """
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False


if __name__ == "__main__":
    try:
        input_year = int(input("Enter a year: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        if is_leap_year(year=input_year):
            print(f"{input_year} is a leap year.")
        else:
            print(f"{input_year} is not a leap year.")
    finally:
        print("Operation completed.")
