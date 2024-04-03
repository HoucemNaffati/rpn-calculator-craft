from .exceptions import CannotApplyRpnCommandException


class Calculation:
    def __init__(self, stack_elements: tuple[int, ...]):
        self.stack_elements = stack_elements

    def add(self) -> tuple[int, ...]:
        return self.__calculate(lambda x, y: x + y)

    def subtract(self) -> tuple[int, ...]:
        return self.__calculate(lambda x, y: x - y)

    def multiply(self) -> tuple[int, ...]:
        return self.__calculate(lambda x, y: x * y)

    def __calculate(self, operation) -> tuple[int, ...]:
        if len(self.stack_elements) < 2:
            raise CannotApplyRpnCommandException
        x, y = self.stack_elements[-2:]
        return self.stack_elements[:-2] + (operation(x, y),)
