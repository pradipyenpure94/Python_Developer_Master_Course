"""Traceback example."""


def calculate_product_price(price: float, quantity: int) -> float:
    """Return the total product price."""
    return price * quantity


def main() -> None:
    price = 15
    quantity = 5
    total = calculate_product_price(price=price, quantity=quantity)
    print(f"Product price: {total:.2f}")


if __name__ == "__main__":
    main()
