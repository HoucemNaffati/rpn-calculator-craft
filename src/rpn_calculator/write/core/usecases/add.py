import dataclasses

from ..ports.stack_repository import StackRepository


@dataclasses.dataclass(frozen=True, kw_only=True)
class AddCommand:
    pass


class AddCommandHandler:
    def __init__(self, stack_repository: StackRepository) -> None:
        self.__stack_repository: StackRepository = stack_repository

    async def handle(self, _: AddCommand) -> None:
        stack = await self.__stack_repository.get()
        stack.add()
        await self.__stack_repository.save(stack)
