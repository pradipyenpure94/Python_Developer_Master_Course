"""Validate product quantity and available stock."""

AVAILABLE_STOCK = 5


def check_available_stock_status(order_quantity: int) -> str:
    if AVAILABLE_STOCK == 0:
        return "Out of Stock"
    elif order_quantity <= AVAILABLE_STOCK:
        return "Available Stock"
    return "Partially Available"


if __name__ == "__main__":
    try:
        order_quantity = int(input("Enter the order quantity: "))
        if order_quantity <= 0:
            raise ValueError("Order quantity must be greater than zero.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        stock_status = check_available_stock_status(
            order_quantity=order_quantity
        )
        print(f"Available Quantity : {AVAILABLE_STOCK}")
        print(f"Order Quantity     : {order_quantity}")
        print(f"Stock Status       : {stock_status}")
