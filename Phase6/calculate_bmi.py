"""Calculate BMI and classify the result using configurable ranges."""

FIRST_BMI_RANGE = 18.5
SECOND_BMI_RANGE = 24.9
THIRD_BMI_RANGE = 29.9
FORTH_BMI_RANGE = 34.9
FIFTH_BMI_RANGE = 39.9


def compute_bmi_category(bmi: float) -> str:
    """Return the BMI category."""
    if bmi < FIRST_BMI_RANGE:
        return "Under Weight"
    if bmi < SECOND_BMI_RANGE:
        return "Healthy / Optimum Weight"
    if bmi < THIRD_BMI_RANGE:
        return "Overweight"
    if bmi < FORTH_BMI_RANGE:
        return "Class I Obesity"
    if bmi < FIFTH_BMI_RANGE:
        return "Class II Obesity (Severe)"
    return "Class II Obesity (Severe)"


try:
    weight = float(input("Enter the weight: "))
    height = float(input("Enter the height: "))

    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be greater than zero.")

    # BMI
    bmi = weight / height ** 2
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print(f"BMI          : {bmi:.2f}")
    print(f"BMI Category : {compute_bmi_category(bmi)}")
