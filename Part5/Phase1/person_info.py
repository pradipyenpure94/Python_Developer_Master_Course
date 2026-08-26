"""Accept a users name and age and display a formatted message."""
MIN_AGE = 10
MAX_AGE = 60


def validate_age(age: int) -> None:
    """Validate that user age."""
    if not MIN_AGE <= age <= MAX_AGE:
        raise ValueError(f"User age must be between {MIN_AGE} and {MAX_AGE}.")


def validate_name(name: str) -> str:
    """Validate that user name."""
    name = " ".join(name.split())
    if not name:
        raise ValueError("Name cannot be empty.")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Name must contain only characters and spaces.")

    return name


try:
    name = input("Enter the name: ").strip()
    name = validate_name(name=name)
    age = int(input("Enter the age: "))
    validate_age(age=age)
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print("-" * 40)
    print("User Information:")
    print("-" * 40)
    print(f"Name  : {name}")
    print(f"Age   : {age} year(s)")
    print("-" * 40)
