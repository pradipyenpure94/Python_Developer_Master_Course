"""Create an electricity bill calculator."""


FIRST_SLAB_LIMIT = 100
SECOND_SLAB_LIMIT = 200
THIRD_SLAB_LIMIT = 300

FIRST_SLAB_RATE = 5
SECOND_SLAB_RATE = 7
THIRD_SLAB_RATE = 10
FOURTH_SLAB_RATE = 15

GST_RATE = 18


def validate_bill_units(units: int) -> None:
    """Validate the bill units."""
    if units < 0:
        raise ValueError("Bill units cannot be negative.")


def calculate_electricity_bill_amount(
    units: int,
    unit_slab_rate: int
) -> float:
    """Calculate the electricity bill amount."""
    amount = units * unit_slab_rate
    return amount


def calculate_electricity_bill(units: int) -> float:
    """Calculate the electricity bill."""
    if units <= FIRST_SLAB_LIMIT:
        return calculate_electricity_bill_amount(
            units=units,
            unit_slab_rate=FIRST_SLAB_RATE
        )
    if units <= SECOND_SLAB_LIMIT:
        return calculate_electricity_bill_amount(
            units=units,
            unit_slab_rate=SECOND_SLAB_RATE
        )
    if units <= THIRD_SLAB_LIMIT:
        return calculate_electricity_bill_amount(
            units=units,
            unit_slab_rate=THIRD_SLAB_RATE
        )
    return calculate_electricity_bill_amount(
        units=units,
        unit_slab_rate=FOURTH_SLAB_RATE
    )


def calculate_amount_with_tax(amount: float) -> float:
    """Calculated total amount including GST."""
    return amount + (amount * GST_RATE / 100)


def main() -> None:
    """Run the main program."""
    try:
        units = int(input("Enter the electricity units: "))
        validate_bill_units(units=units)

        base_bill_amount = calculate_electricity_bill(units=units)
        total_bill_amount = calculate_amount_with_tax(amount=base_bill_amount)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print("Electricity Bill:")
        print(f"No. of Units                : {units}")
        print(f"Base Bill Pay Amount (Rs.)  : {base_bill_amount:.2f}")
        print(f"GST                         : {GST_RATE} %")
        print(f"Total Bill Pay Amount (Rs.) : {total_bill_amount:.2f}")


if __name__ == "__main__":
    main()
