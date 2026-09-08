"""Create custom exception for invalid age."""


class InvalidAge(Exception):
    """Invalid age exception"""


MIN_AGE = 0
MAX_AGE = 120

try:
    age = int(input("Enter the age: "))
    if not MIN_AGE <= age <= MAX_AGE:
        raise InvalidAge(
            f"Person age must be between {MIN_AGE} and {MAX_AGE}."
        )
except (ValueError, InvalidAge) as error:
    print(f"Error: {error}")
else:
    print(f"Person age: {age}")
