from digital_products import DigitalProduct
from Inventory import Inventory
from order import Order
from physical_products import PhysicalProduct
from Product import Product
from Supplier import Supplier


def show_product_details(product: Product) -> None:
    """Works for ANY Product - no subclass checks (LSP)."""
    product.display_information()
    print(f"   Fulfilment: {product.get_fulfilment_info()}")


def main() -> None:
    # ===== Section 2: association (Supplier - Product) =====
    print("\n=== 2. Association: Supplier and Product ===")
    supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
    laptop = PhysicalProduct("P001", "Laptop", 1299.00, 10, supplier, 1.8)
    ebook = DigitalProduct("D001", "Python E-Book", 19.90, 100, supplier,
                           4.5, "https://example.com/python-ebook")

    laptop.supplier.display_information()
    ebook.supplier.display_information()
    print("Same Supplier object shared?", laptop.supplier is ebook.supplier)

    # PREDICT FIRST: what happens after del supplier? Can products still show it?
    del supplier
    print("After 'del supplier':")
    laptop.supplier.display_information()
    ebook.supplier.display_information()

    # ===== Section 3: aggregation (Inventory - Product) =====
    print("\n=== 3. Aggregation: Inventory and Product ===")
    mouse = PhysicalProduct("P002", "Wireless Mouse", 29.90, 50,
                            laptop.supplier, 0.1)   # created BEFORE any inventory
    inventory_a = Inventory("Inventory A")
    inventory_b = Inventory("Inventory B")

    inventory_a.add_product(mouse)
    inventory_a.add_product(laptop)
    inventory_a.display_all_products()

    # PREDICT FIRST: will the Product still work after removal from Inventory A?
    removed = inventory_a.remove_product("P002")
    print("Removed from A:", removed is mouse)
    print("Still in A?", inventory_a.find_product("P002") is not None)
    mouse.display_information()          # still fully usable

    inventory_b.add_product(mouse)       # transfer to B
    inventory_b.display_all_products()
    print("Same object in B as before?", inventory_b.find_product("P002") is mouse)

    # ===== Section 4: composition (Order - OrderLine) =====
    print("\n=== 4. Composition: Order and OrderLine ===")
    order1 = Order("O001")
    order1.add_order_line(laptop, 1)
    order1.add_order_line(mouse, 2)
    order1.display_order()

    # PREDICT FIRST: same Product in two Orders - how many OrderLines / Products?
    order2 = Order("O002")
    order2.add_order_line(mouse, 5)
    order2.display_order()

    line_in_1 = order1.order_lines[1]
    line_in_2 = order2.order_lines[0]
    print("Same OrderLine object?", line_in_1 is line_in_2)
    print("Same Product object?  ", line_in_1.product is line_in_2.product)

    order1.remove_order_line("P002")
    print("\nAfter removing the mouse line from order 1:")
    order1.display_order()
    print("Mouse product still exists:", mouse.name)

    # ===== Section 6: LSP =====
    print("\n=== 6. Substitutability ===")
    show_product_details(laptop)
    show_product_details(ebook)

    inventory_a.add_product(ebook)
    inventory_a.find_product("D001").update_stock(-5)   # normal Product operation
    inventory_a.find_product("P001").update_stock(-2)
    inventory_a.display_all_products()

    # ===== Section 7: polymorphism =====
    print("\n=== 7. Polymorphism ===")
    # PREDICT FIRST: what will get_fulfilment_info() print for each product?
    for product in inventory_a.products:
        product.display_information()
        print(f"   Fulfilment: {product.get_fulfilment_info()}")

    # ===== Persistence (from Lab 7) =====
    print("\n=== Save and reload ===")
    inventory_a.save_to_file("inventory.json")
    reloaded = Inventory("Reloaded")
    reloaded.load_from_file("inventory.json")
    reloaded.display_all_products()


if __name__ == "__main__":
    main()