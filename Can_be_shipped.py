from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface for anything that has to be physically shipped."""

    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass