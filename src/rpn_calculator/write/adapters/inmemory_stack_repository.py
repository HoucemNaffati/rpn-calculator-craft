from ...shared.stack_database import database
from ..core.domain.rpn_stack import RpnStack
from ..core.ports.stack_repository import StackRepository


class InMemoryStackRepository(StackRepository):
    def __init__(self, stack: RpnStack) -> None:
        self.__stack: RpnStack = stack

    async def get(self):
        return self.__stack.clone()

    async def save(self, stack: RpnStack):
        self.__stack = stack.clone()
        database.stack = stack.elements[:]
