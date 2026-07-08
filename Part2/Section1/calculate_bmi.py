"""Calculate BMI."""

# BMI categories as per the WHO standard.
UNDERWEIGHT_LIMIT = 18.5
NORMAL_WEIGHT_LIMIT = 25
OVERWEIGHT_LIMIT = 30

# Height and Weight limits
MIN_HEIGHT = 0.30  # Min. Height (in meter)
MAX_HEIGHT = 3.00  # Max. Height (in meter)
MIN_WEIGHT = 2.00  # Min. Weight (in kg)
MAX_WEIGHT = 500.00  # Max. Weight (in kg)


def get_bmi_category(bmi: float) -> str:
    """
    Return the BMI category.

    Args:
        bmi: Input body mass index (BMI).

    Returns:
        str: The BMI category.
    """
    if bmi < UNDERWEIGHT_LIMIT:
        return "Underweight"
    elif bmi < NORMAL_WEIGHT_LIMIT:
        return "Normal Weight"
    elif bmi < OVERWEIGHT_LIMIT:
        return "Overweight"
    return "Obese"


def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate and return the BMI.

    Args:
        weight (float): Input weight.
        height (float): Input height.

    Returns:
        float: The calculated BMI.
    """
    return weight / (height ** 2)


def validate_input(
    value: float,
    minimum: float,
    maximum: float,
    field_name: str,
    unit: str
) -> None:
    """
    Validate the input value, otherwise raise error message.

    Args:
        value (float): Input value.
        minimum (float): Input minimum value.
        maximum (float): Input maximum value.
        field_name (str): Input parameter name.
        unit (str): Input unit name.

    Raises:
        ValueError: If value not between the min. and max. range.
    """
    if not minimum <= value <= maximum:
        raise ValueError(
            f"{field_name} must be between {minimum:.2f} {unit} and {maximum:.2f} {unit}")


def validate_name(name: str) -> None:
    """
    Validate the user's name.

    Args:
        name (str): Input name.

    Raises:
        ValueError: If the name is empty or contains characters
        other than spaces or letters
    """
    if not name:
        raise ValueError("Name cannot be empty.")
    if not all(ch.isalpha() or ch.isspace() for ch in name):
        raise ValueError("Name must contain only letters and spaces.")


def main():
    """Run the BMI Calculator App."""
    try:
        # Accept inputs from user and its validation
        name = input("Enter the name: ").strip()
        validate_name(name=name)
        weight = float(input("Enter the weight (Kg.): "))
        validate_input(
            value=weight,
            minimum=MIN_WEIGHT,
            maximum=MAX_WEIGHT,
            field_name="Weight",
            unit="kg"
        )

        height = float(input("Enter the height (Meter): "))
        validate_input(
            value=height,
            minimum=MIN_HEIGHT,
            maximum=MAX_HEIGHT,
            field_name="Height",
            unit="m"
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        # To get the BMI
        bmi = calculate_bmi(weight=weight, height=height)
        # To get the BMI category
        category = get_bmi_category(bmi=bmi)

        print("-" * 40)
        print("BMI Report:")
        print("-" * 40)
        print(f"Name     : {name}")
        print(f"Weight   : {weight:.2f} kg")
        print(f"Height   : {height:.2f} m")
        print(f"BMI      : {bmi:.2f}")
        print(f"Category : {category}")
        print("-" * 40)
    finally:
        print("Operation completed.")


if __name__ == "__main__":
    main()
