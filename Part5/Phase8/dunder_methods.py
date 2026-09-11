"""
Implement important dunder methods such as __str__, __len__, __eq__,
and __repr__.
"""


class Product:
    """Represent a product."""

    def __init__(
        self,
        product_id: int,
        name: str,
        price: float,
        quantity: int,
    ) -> None:
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Return the user-friendly product representation."""
        return f"{self.name} - {self.price:.2f}"

    def __repr__(self) -> str:
        """Return the developer-friendly representation."""
        return (
            f"Product("
            f"product_id={self.product_id!r}, "
            f"name={self.name!r}, "
            f"price={self.price!r}, "
            f"quantity={self.quantity!r})"
        )

    def __len__(self) -> int:
        """Return the product quantity."""
        return self.quantity

    def __eq__(self, other: object) -> bool:
        """Compares products using their product ID."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.product_id == other.product_id


def main() -> None:
    """Run the main program."""

    product1 = Product(
        product_id=101,
        name="Laptop",
        price=62500,
        quantity=2
    )

    product2 = Product(
        product_id=102,
        name="Headphone",
        price=2500,
        quantity=2
    )

    print(product1)

    print(repr(product1))

    print(f"Quantity: {len(product1)}")

    print(f"Product1 == Product2: {product1 == product2}")


if __name__ == "__main__":
    main()
