"""__add__() method."""


class Product:
    """Represent a product."""
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __add__(self, other: object) -> tuple[float, str]:
        if not isinstance(other, Product):
            return NotImplemented
        return (self.price + other.price, self.name + other.name)


def main() -> None:
    """Run the main program."""
    product_obj1 = Product(name="Bottle", price=250.5)
    product_obj2 = Product(name="Bag", price=500)
    print(product_obj1 + product_obj2)


if __name__ == "__main__":
    main()
