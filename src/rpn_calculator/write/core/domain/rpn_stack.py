import dataclasses

from .calculation import Calculation


@dataclasses.dataclass(kw_only=True)
class RpnStack:
    elements: tuple[float, ...]

    def append(self, value) -> None:
        self.elements = tuple(self.elements + (value,))

    def clear(self) -> None:
        self.elements = tuple()

    def add(self):
        self.elements = Calculation(self.elements).add()

    def subtract(self):
        self.elements = Calculation(self.elements).subtract()

    def multiply(self):
        self.elements = Calculation(self.elements).multiply()

    def divide(self):
        self.elements = Calculation(self.elements).divide()

    def clone(self):
        return RpnStack(elements=self.elements[:])
