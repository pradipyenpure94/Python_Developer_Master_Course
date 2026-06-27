"""Print all prime numbers between two numbers."""

from check_prime_number import is_prime_number


def get_prime_numbers(start: int = 2, end: int = 50) -> list[int]:
    """
    Return the prime numbers between two input numbers.

    Args:
        start (int): Start input number.
        end (int): End input number.

    Returns:
        list[int]: Prime numbers list.
    """
    return [number for number in range(start, end + 1)
            if is_prime_number(num=number)]


if __name__ == "__main__":
    try:
        start_num = int(input("Enter the start number: "))
        end_num = int(input("Enter the end number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        result = get_prime_numbers(start=start_num, end=end_num)
        print(f"Prime numbers between {start_num} and {end_num}: {result}")
    finally:
        print("Operation completed.")
