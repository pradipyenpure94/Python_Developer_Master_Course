"""Area of rectangle."""


def validate_positive_number(
    parameter_name: str,
    value: float,
) -> None:
    """
    Validate that a numeric value is greater than zero.

    Args:
        parameter_name (str): Name of the input parameter.
        value (float): Numeric value to validate.

    Raises:
        ValueError: If the value is less than or equal to zero.
    """
    if value <= 0:
        raise ValueError(f"{parameter_name} must be greater than zero.")


try:
    # Length of rectangle parameters validation
    length = float(input("Enter the length of rectangle: "))
    validate_positive_number(parameter_name="Length", value=length)

    # Width of rectangle parameters validation
    width = float(input("Enter the width of rectangle: "))
    validate_positive_number(parameter_name="Width", value=width)

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    area_of_rectangle = length * width
    print(f"Area of rectangle: {area_of_rectangle:.2f}")
finally:
    print("Operation completed.")
