"""Voting eligibility."""

# Voting age limits defined, as per the business requirement.
MIN_VOTING_AGE = 18
MAX_VOTING_AGE = 120


def validate_name(name: str) -> None:
    """
    Validate the name.

    Args:
        name (str): Input name.

    Raises:
        ValueError: If the name is empty or
        contains characters other than letters and spaces.
    """
    if not name:
        raise ValueError("Name cannot be empty.")
    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError("Name must contain only letters and spaces.")


def validate_age(age: int) -> None:
    """
    Validate the user's age.

    Args:
        age (int): Input age.

    Raises:
        ValueError: If age is outside the valid range.
    """
    if not 1 <= age <= MAX_VOTING_AGE:
        raise ValueError(f"Age must be between 1 and {MAX_VOTING_AGE} years.")


def is_eligible_to_vote(age: int) -> bool:
    """
    Check whether a person is eligible to vote.

    Args:
        age (int): Input age.

    Returns:
        bool: True if the person is eligible to vote, otherwise False.
    """
    return MIN_VOTING_AGE <= age <= MAX_VOTING_AGE


def print_voting_eligibility_report(name: str, age: int, status: bool) -> None:
    """
    Print the voting eligibility report.

    Args:
        name (str): Input name.
        age (int): Input age.
        status (bool): True if the person is eligible to vote, otherwise False.
    """
    status = "Eligible to vote" if status else "Not eligible to vote"
    print("-" * 40)
    print("Voting Eligibility Report:")
    print("-" * 40)
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Status : {status}")
    print("-" * 40)


def main() -> None:
    """Run the voting eligibility report application."""
    try:
        # Accept input from user and its validation.
        name = input("Enter the name: ").strip()
        validate_name(name=name)
        age = int(input("Enter the age: "))
        validate_age(age=age)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        # To get the status of voting eligibility.
        status = is_eligible_to_vote(age=age)
        # Print voting eligibility report.
        print_voting_eligibility_report(name=name, age=age, status=status)
    finally:
        print("Operation completed.")


if __name__ == "__main__":
    main()
