from rpn_calculator.write.adapters.inmemory_stack_repository import (
    InMemoryStackRepository,
)
from rpn_calculator.write.core.domain.rpn_stack import RpnStack
from rpn_calculator.write.core.ports.stack_repository import StackRepository


def get_stack_repository() -> StackRepository:
    return InMemoryStackRepository(RpnStack(values=()))
