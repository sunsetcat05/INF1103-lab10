from Product import Product


class OrderLine:
    """One product + quantity inside ONE order.

    Created only by Order.add_order_line(). It refers to a Product (association)
    but does not own it.
    """

    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        self._product: Product = product
        self._quantity: int = quantity

    @property
    def product(self) -> Product:
        return self._product

    @property
    def quantity(self) -> int:
        return self._quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

    def display_information(self) -> None:
        print(f"   {self.product.name} x {self.quantity} "
              f"@ ${self.product.price:.2f} = ${self.calculate_subtotal():.2f}")