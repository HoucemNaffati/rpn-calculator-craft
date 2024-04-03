import dataclasses

from .calculation import Calculation


@dataclasses.dataclass(kw_only=True)
class RpnStack:
    elements: tuple[int, ...]

    def append(self, value) -> None:
        self.elements = tuple(self.elements + (value,))

    def add(self):
        self.elements = Calculation(self.elements).add()

    def subtract(self):
        self.elements = Calculation(self.elements).subtract()

    def clone(self):
        return RpnStack(elements=self.elements[:])
