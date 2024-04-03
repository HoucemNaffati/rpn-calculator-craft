from abc import ABC, abstractmethod

from rpn_calculator.write.core.domain.rpn_stack import RpnStack


class StackRepository(ABC):
    @abstractmethod
    async def get(self) -> RpnStack:
        raise NotImplementedError

    @abstractmethod
    async def save(self, stack: RpnStack) -> None:
        raise NotImplementedError
