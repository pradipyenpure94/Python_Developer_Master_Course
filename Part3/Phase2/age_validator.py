"""
Age Validator — Static Method

Create a static method:

    is_valid_age(age)

Return True or False.
"""


class AgeValidator:
    """Validate an age."""

    @staticmethod
    def is_valid_age(age: int) -> bool:
        """Return True if age is between 0 and 120, otheriwse False."""
        return age >= 0 and age <= 120


def main() -> None:
    """Run the main program."""
    age = -33
    print(f"{AgeValidator.is_valid_age(age=age)}")


if __name__ == "__main__":
    main()
