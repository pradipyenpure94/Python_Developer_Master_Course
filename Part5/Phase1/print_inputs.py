"""Print your name, age, city and profession."""

MIN_AGE = 1
MAX_AGE = 120


def validate_age(age: int) -> int:
    """Validate the age."""
    if not MIN_AGE <= age <= MAX_AGE:
        raise ValueError(f"Age must be between {MIN_AGE} and {MAX_AGE}.")
    return age


def validate_field_value(field_name: str, value: str) -> str:
    """Validate the field value."""
    value = " ".join(value.split())
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")
    is_valid = value.replace(" ", "").isalpha()
    if not is_valid:
        raise ValueError(
            f"{field_name} must contain only characters and spaces."
        )
    return value


def main() -> None:
    """Run the main program."""
    try:
        # Accept and validate person name
        name = input("Enter the name: ")
        name = validate_field_value(field_name="Name", value=name)
        # Accept and validate person age
        age = int(input("Enter the age: "))
        age = validate_age(age=age)
        # Accept and validate person city
        city = input("Enter the city: ")
        city = validate_field_value(field_name="City", value=city)
        # Accept and validate person profession
        profession = input("Enter the profession: ")
        profession = validate_field_value(
            field_name="Profession",
            value=profession
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print("-" * 40)
        print("Person Information:")
        print("-" * 40)
        print(f"Name         : {name}")
        print(f"Age          : {age}")
        print(f"City         : {city}")
        print(f"Profession   : {profession}")
        print("-" * 40)


if __name__ == "__main__":
    main()
