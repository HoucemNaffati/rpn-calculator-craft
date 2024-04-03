import dataclasses
from typing import cast

from .exceptions import CannotApplyRpnCommandException


@dataclasses.dataclass(kw_only=True)
class RpnStack:
    elements: tuple[int, ...]

    def append(self, value) -> None:
        self.elements = tuple(self.elements + (value,))

    def add(self):
        operable_pair = OperablePair(stack_elements=self.elements)
        pair_sum = operable_pair.sum()
        self.__flush(pair_sum)

    def clone(self):
        return RpnStack(elements=self.elements[:])

    def __flush(self, result: tuple[int]) -> None:
        self.elements = self.__cold_sub_stack_elements() + result

    def __cold_sub_stack_elements(self) -> tuple[int, ...]:
        return self.elements[:-2]


@dataclasses.dataclass(kw_only=True)
class OperablePair:
    __pair: tuple[int, int]

    def __init__(self, stack_elements: tuple[int, ...]):
        if len(stack_elements) < 2:
            raise CannotApplyRpnCommandException
        self.__pair = cast(tuple[int, int], stack_elements[-2:])

    def sum(self) -> tuple[int]:
        return ((sum(self.__pair)),)
