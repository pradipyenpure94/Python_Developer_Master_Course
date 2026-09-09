"""Create a product class with private price."""


class Product:
    """Represent a product."""

    def __init__(self, price: float) -> None:
        self.__price = price
