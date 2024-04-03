from typing import Union

import pytest

from rpn_calculator.write.adapters.inmemory_stack_repository import (
    InMemoryStackRepository,
)
from rpn_calculator.write.core.domain.rpn_stack import RpnStack
from src.rpn_calculator.write.core.ports.stack_repository import StackRepository
from src.rpn_calculator.write.core.usecases.clear import (
    ClearCommand,
    ClearCommandHandler,
)


@pytest.mark.asyncio
async def test_clear_when_stack_is_empty():
    await verify_clear_stack(
        command=ClearCommand(), expected_stack=RpnStack(elements=())
    )


@pytest.mark.asyncio
async def test_append_when_stack_is_full():
    await verify_clear_stack(
        command=ClearCommand(),
        expected_stack=RpnStack(elements=()),
        initial_stack=RpnStack(elements=(1, 2)),
    )


async def verify_clear_stack(
    command: ClearCommand,
    expected_stack: RpnStack,
    initial_stack=RpnStack(elements=()),
) -> None:
    stack_repository: Union[StackRepository, InMemoryStackRepository] = (
        InMemoryStackRepository(initial_stack)
    )
    use_case = ClearCommandHandler(stack_repository)
    await use_case.handle(command)
    actual_stack = await stack_repository.get()
    assert actual_stack == expected_stack
