from abc import ABC, abstractmethod

from Supplier import Supplier


class Product(ABC):
    """Abstract parent of every item an Inventory can hold."""

    def __init__(self, product_id: str, name: str, price: float,
                 stock_quantity: int, supplier: Supplier):
        self._product_id: str = product_id
        self._name: str = name
        self._price: float = 0.0
        self._stock_quantity: int = 0
        self.price = price                      # validated by the setter
        self.stock_quantity = stock_quantity    # validated by the setter
        # ASSOCIATION: the Product knows its Supplier, it does not own it.
        self._supplier: Supplier = supplier

    # ---- properties ------------------------------------------------------
    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @property
    def stock_quantity(self) -> int:
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value: int) -> None:
        if value < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self._stock_quantity = value

    @property
    def supplier(self) -> Supplier:
        return self._supplier

    # ---- behaviour every Product promises (LSP) ---------------------------
    def update_stock(self, quantity: int) -> None:
        """Change stock by `quantity` (positive adds, negative removes).

        Neither subclass overrides this with different rules, so any code
        written against Product can rely on the same meaning.
        """
        self.stock_quantity = self._stock_quantity + quantity

    def display_information(self) -> None:
        print(f"ID: {self.product_id} | {self.name} | ${self.price:.2f} | "
              f"Stock: {self.stock_quantity} | Supplier: {self.supplier.name}")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Each product type describes how it reaches the customer."""

    def to_dict(self) -> dict:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock_quantity": self.stock_quantity,
            "supplier": self.supplier.to_dict(),
        }

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict, supplier: Supplier) -> "Product":
        """Rebuild a product from saved data, using an existing Supplier."""