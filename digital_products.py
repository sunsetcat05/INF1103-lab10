from Product import Product
from Supplier import Supplier


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float,
                 stock_quantity: int, supplier: Supplier,
                 file_size_mb: float, download_url: str):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self._file_size_mb: float = file_size_mb
        self._download_url: str = download_url

    @property
    def file_size_mb(self) -> float:
        return self._file_size_mb

    @property
    def download_url(self) -> str:
        return self._download_url

    # update_stock() is deliberately NOT overridden. Here "stock" means
    # licences/keys available, so the inherited meaning still holds (LSP).

    def display_information(self) -> None:
        super().display_information()
        print(f"   Type: Digital | File size: {self.file_size_mb} MB")

    def get_fulfilment_info(self) -> str:
        return (f"Instant download, link emailed after purchase. "
                f"File size: {self.file_size_mb} MB")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["file_size_mb"] = self.file_size_mb
        data["download_url"] = self.download_url
        return data

    @classmethod
    def from_dict(cls, data: dict, supplier: Supplier) -> "DigitalProduct":
        return cls(data["product_id"], data["name"], data["price"],
                   data["stock_quantity"], supplier,
                   data["file_size_mb"], data["download_url"])