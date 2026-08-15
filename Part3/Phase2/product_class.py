"""
Product Class

Create a Product class with:

    product ID
    name
    price

Create multiple products.
"""


class Product:
    """Represent a product."""

    def __init__(self, product_id: int, name: str, price: float) -> None:
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product_info(self) -> None:
        """Display product information."""
        print("-" * 40)
        print("Product Information:")
        print("-" * 40)
        print(f"Product ID  : {self.product_id}")
        print(f"Name        : {self.name}")
        print(f"Price       : {self.price:.2f}")
        print("-" * 40)


products = []

product1 = Product(product_id=101, name="School Bag", price=450)
products.append(product1)

product2 = Product(product_id=102, name="Pen", price=14.5)
products.append(product2)

product3 = Product(product_id=103, name="Water Bootle", price=120.56)
products.append(product3)

for product in products:
    product.display_product_info()
