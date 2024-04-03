import pytest

from src.rpn_calculator.write.adapters.inmemory_stack_repository import (
    InMemoryStackRepository,
)
from src.rpn_calculator.write.core.domain.exceptions import (
    CannotApplyRpnCommandException,
)
from src.rpn_calculator.write.core.domain.rpn_stack import RpnStack
from src.rpn_calculator.write.core.usecases.subtract import (
    SubtractCommand,
    SubtractCommandHandler,
)


@pytest.mark.asyncio
async def test_subtract_command_when_the_stack_has_exactly_two_values():
    await verify_subtract_command(
        command=SubtractCommand(),
        expected_stack=RpnStack(elements=(-1,)),
        initial_stack=RpnStack(elements=(1, 2)),
    )


@pytest.mark.asyncio
async def test_subtract_command_when_the_stack_has_more_than_two_values():
    await verify_subtract_command(
        command=SubtractCommand(),
        expected_stack=RpnStack(elements=(1, 3)),
        initial_stack=RpnStack(elements=(1, 2, -1)),
    )


@pytest.mark.asyncio
async def test_subtract_command_when_the_stack_has_one_value():
    await verify_subtract_command_failure(
        exception=CannotApplyRpnCommandException, initial_stack=RpnStack(elements=(1,))
    )


@pytest.mark.asyncio
async def test_subtract_command_when_the_stack_is_empty():
    await verify_subtract_command_failure(
        exception=CannotApplyRpnCommandException, initial_stack=RpnStack(elements=())
    )


async def verify_subtract_command(
    command: SubtractCommand,
    expected_stack: RpnStack,
    initial_stack=RpnStack(elements=()),
) -> None:
    stack_repository = InMemoryStackRepository(initial_stack)
    use_case = SubtractCommandHandler(stack_repository)
    await use_case.handle(command)
    actual_stack = await stack_repository.get()
    assert actual_stack == expected_stack


async def verify_subtract_command_failure(exception, initial_stack):
    with pytest.raises(exception):
        await verify_subtract_command(
            SubtractCommand(), RpnStack(elements=(1, 1, 1, 1, 1)), initial_stack
        )
