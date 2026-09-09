"""
1. Create a product class with private price.
2. Validate Product using Encapsulation.
"""

MIN_PRICE = 100
MAX_PRICE = 500


class Product:
    """Represent a product."""

    def __init__(self, price: float) -> None:
        self.set_product_price(price=price)

    def get_product_price(self) -> float:
        """Return the product price."""
        return self.__price

    def set_product_price(self, price: float) -> None:
        """Validate and update the product price."""
        if not MIN_PRICE <= price <= MAX_PRICE:
            raise ValueError(
                f"Product price must be between {MIN_PRICE} and {MAX_PRICE}."
            )

        self.__price = price


try:
    product_obj = Product(price=105)
except ValueError as error:
    print(f"Error: {error}")
else:
    print(f"Current Product Price: {product_obj.get_product_price()}")
