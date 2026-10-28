"""Create an order approval rule using multiple conditions."""

customer_account_status = True
stock_quantity = 5


def customer_order_approval(
    customer_account_status: bool,
    order_quantity: int
) -> str:
    if not customer_account_status:
        return "Order Rejected"
    if order_quantity <= 0:
        return "Invalid Order."
    elif stock_quantity <= 0:
        return "Out of Stock"
    elif order_quantity > stock_quantity:
        return "Partially Available"
    elif stock_quantity >= order_quantity:
        can_approve = input(
            "Confirm for order approve ('yes' or 'no'): "
        ).strip().casefold()
        if can_approve == "yes":
            return "Order Approved"
        return "Order On Hold"


if __name__ == "__main__":
    result = customer_order_approval(
        customer_account_status=customer_account_status,
        order_quantity=5
    )
    print(result)
