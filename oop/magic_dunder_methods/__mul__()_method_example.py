"""__mul__() method."""


class Product:
    """Represent a product."""
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __mul__(self, quantity: object) -> float:
        if not isinstance(quantity, (float, int)):
            return NotImplemented
        return self.price * quantity


def main() -> None:
    """Run the main program."""
    product_obj = Product(name="Bottle", price=350)
    total_price = product_obj * 3
    print(f"Total product price: {total_price:.2f}")


if __name__ == "__main__":
    main()
