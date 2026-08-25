"""Calculate the compound interest."""


from calculate_simple_interest import validate_non_negative_value


def validate_compounding_frequency(frequency: int) -> None:
    """Validate that the compounding frequency is greater than zero."""
    if frequency <= 0:
        raise ValueError("Compound frequency must be greater than zero.")


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
        compounding_frequency = int(input("Enter the compounding frequency (N): "))
        validate_compounding_frequency(frequency=compounding_frequency)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        amount = principal_amount * (
            1 + rate_of_interest
            / (100 * compounding_frequency)
            ) ** (compounding_frequency * time)
        print(f"Total Amount with Interest: {amount:.2f}")

        compound_interest = amount - principal_amount
        print(f"Compound Interest (CI): {compound_interest:.2f}")


if __name__ == "__main__":
    main()
