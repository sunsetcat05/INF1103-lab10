class Supplier:
    """Someone who supplies products. Exists independently of any Product."""

    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self._supplier_id: str = supplier_id
        self._name: str = name
        self._contact_email: str = contact_email

    @property
    def supplier_id(self) -> str:
        return self._supplier_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def contact_email(self) -> str:
        return self._contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.supplier_id} | Name: {self.name} | "
              f"Email: {self.contact_email}")

    def to_dict(self) -> dict:
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "contact_email": self.contact_email,
        }