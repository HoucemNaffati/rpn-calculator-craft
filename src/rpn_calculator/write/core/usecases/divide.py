import dataclasses

from ..ports.stack_repository import StackRepository


@dataclasses.dataclass(frozen=True, kw_only=True)
class DivideCommand:
    pass


class DivideCommandHandler:
    def __init__(self, stack_repository: StackRepository) -> None:
        self.__stack_repository: StackRepository = stack_repository

    async def handle(self, _: DivideCommand) -> None:
        stack = await self.__stack_repository.get()
        stack.divide()
        await self.__stack_repository.save(stack)
