"""
Product Price Protection

Make product price private.

Prevent:

    - negative price
    - zero price
"""


class Product:
    """Represent a product."""
    def __init__(self, price: float) -> None:
        self.set_price(price=price)

    def get_price(self) -> float:
        """Return the product price."""
        return self.__price

    def set_price(self, price: float) -> None:
        """Set to the product price."""
        if price <= 0:
            raise ValueError("Product price must be greater than zero.")
        self.__price = price


def main() -> None:
    """Run the main program."""
    try:
        price = float(input("Enter the product price: "))
        product_obj = Product(price=price)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Product price: {product_obj.get_price():.2f}")


if __name__ == "__main__":
    main()
