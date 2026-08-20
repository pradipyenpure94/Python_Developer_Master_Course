"""
__lt__() and __gt__()

Create a Product class and compare products based on price:

    product1 < product2
    product1 > product2
"""


class Product:
    """Represent a product."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price


def main() -> None:
    """Run the main program."""
    product1 = Product(name="Pen", price=10)
    product2 = Product(name="Pencil", price=3)

    print(product1 < product2)
    print(product1 > product2)


if __name__ == "__main__":
    main()
