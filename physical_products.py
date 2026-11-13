from Can_be_shipped import CanBeShipped
from Product import Product
from Supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float,
                 stock_quantity: int, supplier: Supplier, weight_kg: float):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self._weight_kg: float = weight_kg

    @property
    def weight_kg(self) -> float:
        return self._weight_kg

    def calculate_shipping_cost(self) -> float:
        return 5.00 + 2.00 * self._weight_kg

    def display_information(self) -> None:
        super().display_information()
        print(f"   Type: Physical | Weight: {self.weight_kg} kg")

    def get_fulfilment_info(self) -> str:
        return (f"Shipped to your address. Weight: {self.weight_kg} kg, "
                f"shipping cost: ${self.calculate_shipping_cost():.2f}")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight_kg"] = self.weight_kg
        return data

    @classmethod
    def from_dict(cls, data: dict, supplier: Supplier) -> "PhysicalProduct":
        return cls(data["product_id"], data["name"], data["price"],
                   data["stock_quantity"], supplier, data["weight_kg"])