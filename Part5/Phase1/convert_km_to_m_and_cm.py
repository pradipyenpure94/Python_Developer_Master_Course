"""Convert kilometers to meters and centimeters."""


METERS_PER_KILOMETER = 1000
CENTIMETERS_PER_KILOMETER = 100000


def validate_kilometers(kilometers: float) -> None:
    """Validate the kilometers."""
    if kilometers < 0:
        raise ValueError("Kilometers cannot be negative.")


try:
    kilometers = float(input("Enter the kilometers(KM): "))
    validate_kilometers(kilometers=kilometers)

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    meters = kilometers * METERS_PER_KILOMETER
    print(f"METERS       : {meters:.2f}")
    centimeters = kilometers * CENTIMETERS_PER_KILOMETER
    print(f"CENTIMETERS  : {centimeters:.2f}")
