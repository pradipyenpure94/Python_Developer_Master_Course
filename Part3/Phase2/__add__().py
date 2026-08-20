"""
__add__()

Create a ShoppingCart class.

Use:

    cart1 + cart2

to combine the total prices/items of two carts.
"""


class ShoppingCart:
    """Represent a shopping cart."""

    def __init__(self, total_price: float, item_count: int) -> None:
        self.total_price = total_price
        self.item_count = item_count

    def __add__(self, other: object) -> "ShoppingCart":
        if not isinstance(other, ShoppingCart):
            return NotImplemented

        return ShoppingCart(
            total_price=self.total_price + other.total_price,
            item_count=self.item_count + other.item_count
        )

    def display_cart_info(self) -> None:
        """Display shopping cart information."""
        print(f"Total price: {self.total_price:.2f}")
        print(f"Item count: {self.item_count}")


def main() -> None:
    """Run the main program."""
    shopping_cart1 = ShoppingCart(total_price=100, item_count=1)
    shopping_cart2 = ShoppingCart(total_price=5, item_count=5)

    combined_cart = shopping_cart1 + shopping_cart2
    combined_cart.display_cart_info()


if __name__ == "__main__":
    main()
