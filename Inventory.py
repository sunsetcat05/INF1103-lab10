import json
import os

from digital_products import DigitalProduct
from physical_products import PhysicalProduct
from Product import Product
from Supplier import Supplier

# Only place that has to know the concrete types: turning saved data back
# into objects. Everything else works through the Product abstraction.
PRODUCT_TYPES: dict[str, type[Product]] = {
    "physical": PhysicalProduct,
    "digital": DigitalProduct,
}


class Inventory:
    """AGGREGATION: groups Product objects but does not own their lifecycle."""

    def __init__(self, name: str = "Inventory"):
        self.name: str = name
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        if self.find_product(product.product_id) is not None:
            print(f"[{self.name}] Product {product.product_id} already exists.")
            return
        self.products.append(product)

    def remove_product(self, product_id: str) -> Product | None:
        """Remove the reference only; the Product itself lives on.

        The removed Product is returned so it can be reused or transferred.
        """
        product = self.find_product(product_id)
        if product is not None:
            self.products.remove(product)
        return product

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def display_all_products(self) -> None:
        # No isinstance() checks: each Product displays itself (LSP + polymorphism).
        print(f"--- {self.name} ({len(self.products)} products) ---")
        for product in self.products:
            product.display_information()

    # ---- JSON persistence (carried over from Lab 7, now with suppliers) ----
    def save_to_file(self, filename: str = "inventory.json") -> None:
        data = [product.to_dict() for product in self.products]
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename: str = "inventory.json") -> None:
        if not os.path.exists(filename):
            print(f"{filename} not found, starting with an empty inventory.")
            return
        with open(filename, "r") as file:
            data: list[dict] = json.load(file)

        suppliers: dict[str, Supplier] = {}   # one shared Supplier per id
        self.products = []
        for item in data:
            s = item["supplier"]
            if s["supplier_id"] not in suppliers:
                suppliers[s["supplier_id"]] = Supplier(
                    s["supplier_id"], s["name"], s["contact_email"])
            product_class = PRODUCT_TYPES[item["type"]]
            self.products.append(
                product_class.from_dict(item, suppliers[s["supplier_id"]]))