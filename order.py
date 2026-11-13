from order_line import OrderLine
from Product import Product


class Order:
    """COMPOSITION: an Order creates, manages and owns its OrderLines."""

    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self._order_lines: list[OrderLine] = []

    @property
    def order_lines(self) -> list[OrderLine]:
        # A copy, so outside code can't append OrderLines it created itself.
        return list(self._order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)   # the Order creates its own lines
        self._order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> None:
        self._order_lines = [line for line in self._order_lines
                             if line.product.product_id != product_id]

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self._order_lines)

    def display_order(self) -> None:
        print(f"Order {self.order_id}:")
        for line in self._order_lines:
            line.display_information()
        print(f"   Total: ${self.calculate_total():.2f}")