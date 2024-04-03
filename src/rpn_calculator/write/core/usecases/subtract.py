import dataclasses

from ..ports.stack_repository import StackRepository


@dataclasses.dataclass(frozen=True, kw_only=True)
class SubtractCommand:
    pass


class SubtractCommandHandler:
    def __init__(self, stack_repository: StackRepository) -> None:
        self.__stack_repository: StackRepository = stack_repository

    async def handle(self, _: SubtractCommand) -> None:
        stack = await self.__stack_repository.get()
        stack.subtract()
        await self.__stack_repository.save(stack)
