from .exceptions import CannotApplyRpnCommandException, DivisionByZeroException


class Calculation:
    def __init__(self, stack_elements: tuple[float, ...]):
        self.stack_elements = stack_elements

    def add(self) -> tuple[float, ...]:
        return self.__calculate(lambda x, y: x + y)

    def subtract(self) -> tuple[float, ...]:
        return self.__calculate(lambda x, y: x - y)

    def multiply(self) -> tuple[float, ...]:
        return self.__calculate(lambda x, y: x * y)

    def divide(self) -> tuple[float, ...]:
        def division_operation(x, y) -> float:
            if y == 0:
                raise DivisionByZeroException
            return x / y

        return self.__calculate(division_operation)

    def __calculate(self, operation) -> tuple[float, ...]:
        if len(self.stack_elements) < 2:
            raise CannotApplyRpnCommandException
        x, y = self.stack_elements[-2:]
        return self.stack_elements[:-2] + (operation(x, y),)
