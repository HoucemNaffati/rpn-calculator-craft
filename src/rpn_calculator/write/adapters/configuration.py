from functools import lru_cache

from ..core.domain.rpn_stack import RpnStack
from ..core.ports.stack_repository import StackRepository
from .inmemory_stack_repository import InMemoryStackRepository


@lru_cache
def get_stack_repository() -> StackRepository:
    return InMemoryStackRepository(RpnStack(elements=()))
