from rpn_calculator.write.core.domain.rpn_stack import RpnStack
from rpn_calculator.write.core.ports.stack_repository import StackRepository


class InMemoryStackRepository(StackRepository):
    def __init__(self, stack: RpnStack):
        self.__stack: RpnStack = stack

    async def get(self):
        return self.__stack.clone()

    async def save(self, stack: RpnStack):
        self.__stack = stack.clone()
