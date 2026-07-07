"""Calculate electricity bill."""

from datetime import date

# Default charges for electricity calculation.
FIXED_CHARGES = 50.00  # Maintenance charges
LATE_PAYMENT_CHARGES = 10.00  # Applicable after the due date
SUBSIDY = 50.00
GST = 18

# Default units slabs
SLAB_1_LIMIT = 100
SLAB_2_LIMIT = 200

# Default rate per unit
SLAB_1_RATE = 5.0
SLAB_2_RATE = 7.0
SLAB_3_RATE = 10.0

# Last pay bill due date.
DUE_DATE = date(2026, 7, 25)

# Current date.
TODAY_DATE = date(2026, 7, 2)


def calculate_consumption_charges(units: int) -> float:
    """
    Calculate the electricity charges based on consumed units.

    Args:
        units (int): Number of electricity units consumed.

    Returns:
        float: Calculated electricity charges.
    """

    if units <= SLAB_1_LIMIT:
        return units * SLAB_1_RATE
    elif units <= SLAB_2_LIMIT:
        return units * SLAB_2_RATE
    return units * SLAB_3_RATE


def calculate_gst(consume_charges: float) -> float:
    """
    Calculate GST based on the electricity charges.

    Args:
        consume_charges (float): Electricity consumption charges.

    Returns:
        float: Calculated GST amount.
    """
    return consume_charges * GST / 100


try:
    # Accept power consumer name from user input.
    consumer_name = input("Enter the consumer name: ").strip()
    if not consumer_name:
        raise ValueError("Name cannot be empty.")

    # Accept consume units input from the user.
    units = int(input("Enter the power consumed units (int): "))
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")

    # Accept last month pending bill amount from the user.
    pending_bill_amount = float(
        input("Enter the last month pending bill amount: "))
    if pending_bill_amount < 0:
        raise ValueError("Pending bill amount cannot be negative.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    # Calculation of consume power charges.
    consume_charges = calculate_consumption_charges(units=units)
    gst_amount = calculate_gst(consume_charges=consume_charges)
    other_charges = FIXED_CHARGES + pending_bill_amount

    if TODAY_DATE > DUE_DATE:
        other_charges += LATE_PAYMENT_CHARGES

    # Total pay bill amount.
    total_bill = consume_charges + gst_amount + other_charges - SUBSIDY
    print("\n")
    print("Electricity Bill:")
    print("-" * 50)
    print(f"Consumer name             : {consumer_name}")
    print(f"Units consumed            : {units}")
    print(f"Energy charges            : {consume_charges:.2f}")
    print(f"GST ({GST}%)                 : {gst_amount:.2f}")
    print(f"Fixed Charges             : {FIXED_CHARGES:.2f}")
    print(f"Pending Amount            : {pending_bill_amount:.2f}")
    if TODAY_DATE > DUE_DATE:
        print(f"Late Payment Fee          : {LATE_PAYMENT_CHARGES:.2f}")
    print(f"Subsidy                   : -{SUBSIDY:.2f}")
    print("-" * 50)
    print(f"Total Pay Bill Amount     : {total_bill:.2f}")
finally:
    print("Operation completed.")
