import pytest

from rpn_calculator.write.adapters.inmemory_stack_repository import (
    InMemoryStackRepository,
)
from rpn_calculator.write.core.domain.rpn_stack import RpnStack
from rpn_calculator.write.core.usecases.append import (
    AppendCommand,
    AppendCommandHandler,
)


@pytest.mark.asyncio
async def test_append_when_stack_is_empty():
    await verify_append_stack(
        command=AppendCommand(value=0), expected_stack=RpnStack(values=(0,))
    )


@pytest.mark.asyncio
async def test_append_when_stack_is_full_with_unique_values():
    await verify_append_stack(
        command=AppendCommand(value=-1),
        expected_stack=RpnStack(values=(1, 2, -1)),
        initial_stack=RpnStack(values=(1, 2)),
    )


@pytest.mark.asyncio
async def test_append_when_stack_is_full_with_duplicate_values():
    await verify_append_stack(
        command=AppendCommand(value=1),
        expected_stack=RpnStack(values=(1, 1, 2, 1)),
        initial_stack=RpnStack(values=(1, 1, 2)),
    )


async def verify_append_stack(
    command: AppendCommand, expected_stack: RpnStack, initial_stack=RpnStack(values=())
) -> None:
    stack_repository = InMemoryStackRepository(initial_stack)
    use_case = AppendCommandHandler(stack_repository)
    await use_case.handle(command)
    actual_stack = await stack_repository.get()
    assert actual_stack == expected_stack
