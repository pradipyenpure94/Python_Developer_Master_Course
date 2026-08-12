"""Create a Product class with multiple objects."""


class Product:
    """Represent a product."""
    def __init__(self, product_name: str) -> None:
        self.product_name = product_name

    def __str__(self):
        return f"Product Name: {self.product_name}"


def main() -> None:
    """Run the main program."""
    product_obj_one = Product(product_name="Laptop")
    print(product_obj_one)
    product_obj_two = Product(product_name="Nokia Mobile")
    print(product_obj_two)


if __name__ == "__main__":
    main()
