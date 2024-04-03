import dataclasses

from rpn_calculator.write.core.ports.stack_repository import StackRepository


@dataclasses.dataclass(frozen=True, kw_only=True)
class AppendCommand:
    value: int


class AppendCommandHandler:
    def __init__(self, stack_repository: StackRepository) -> None:
        self.__stack_repository: StackRepository = stack_repository

    async def handle(self, command: AppendCommand) -> None:
        stack = await self.__stack_repository.get()
        stack.append(command.value)
        await self.__stack_repository.save(stack)
