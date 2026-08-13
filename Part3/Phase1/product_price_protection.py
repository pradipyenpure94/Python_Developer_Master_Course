"""Product price protection using encapsulation and business Logic."""

MIN_PRICE = 100
MAX_PRICE = 5000


def validate_product_price(price: float) -> None:
    """Validate the product price."""
    if not MIN_PRICE <= price <= MAX_PRICE:
        raise ValueError(
            f"Product price must be between {MIN_PRICE} "
            f"and {MAX_PRICE}."
        )


class Product:
    """Represent a product."""
    def __init__(self, price: float) -> None:
        self.price = price

    @property
    def price(self) -> float:
        """Return the product price."""
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        validate_product_price(price=price)
        self.__price = price


def main() -> None:
    """Run the main program."""
    try:
        product_price = float(input("Enter the product price: "))
        product_obj = Product(price=product_price)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Product price: {product_obj.price}")


if __name__ == "__main__":
    main()
