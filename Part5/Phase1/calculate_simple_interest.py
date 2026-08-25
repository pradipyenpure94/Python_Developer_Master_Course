"""Calculate simple interest."""


def validate_non_negative_value(field_name: str, value: float) -> None:
    """Validate that value is not negative."""
    if value < 0:
        raise ValueError(f"{field_name} cannot be negative.")


def main() -> None:
    """Run the main program."""
    try:
        principal_amount = float(input("Enter the principal amount (P): "))
        validate_non_negative_value(
            field_name="Principal amount",
            value=principal_amount
        )
        rate_of_interest = float(input("Enter the rate of interest (ROI) %: "))
        validate_non_negative_value(
            field_name="Rate of Interest",
            value=rate_of_interest
        )
        time = float(input("Enter the time duration (in years): "))
        validate_non_negative_value(field_name="Time", value=time)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        simple_interest = (principal_amount * rate_of_interest * time) / 100
        print(f"Simple Interest (SI): {simple_interest:.2f}")


if __name__ == "__main__":
    main()
