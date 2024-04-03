import pytest

from src.rpn_calculator.write.adapters.inmemory_stack_repository import (
    InMemoryStackRepository,
)
from src.rpn_calculator.write.core.domain.exceptions import (
    CannotApplyRpnCommandException,
    DivisionByZeroException,
)
from src.rpn_calculator.write.core.domain.rpn_stack import RpnStack
from src.rpn_calculator.write.core.usecases.divide import (
    DivideCommand,
    DivideCommandHandler,
)


@pytest.mark.asyncio
async def test_divide_command_when_the_stack_has_exactly_two_values():
    await verify_divide_command(
        command=DivideCommand(),
        expected_stack=RpnStack(elements=(0.5,)),
        initial_stack=RpnStack(elements=(1, 2)),
    )


@pytest.mark.asyncio
async def test_divide_command_when_the_stack_has_more_than_two_values():
    await verify_divide_command(
        command=DivideCommand(),
        expected_stack=RpnStack(elements=(1, 0)),
        initial_stack=RpnStack(elements=(1, 0, -1)),
    )


@pytest.mark.asyncio
async def test_divide_command_when_the_stack_has_one_value():
    await verify_divide_command_failure(
        exception=CannotApplyRpnCommandException, initial_stack=RpnStack(elements=(1,))
    )


@pytest.mark.asyncio
async def test_divide_command_when_the_stack_is_empty():
    await verify_divide_command_failure(
        exception=CannotApplyRpnCommandException, initial_stack=RpnStack(elements=())
    )


@pytest.mark.asyncio
async def test_divide_command_when_the_stack_tail_is_zero():
    await verify_divide_command_failure(
        exception=DivisionByZeroException, initial_stack=RpnStack(elements=(1, 2, 0))
    )


async def verify_divide_command(
    command: DivideCommand,
    expected_stack: RpnStack,
    initial_stack=RpnStack(elements=()),
) -> None:
    stack_repository = InMemoryStackRepository(initial_stack)
    use_case = DivideCommandHandler(stack_repository)
    await use_case.handle(command)
    actual_stack = await stack_repository.get()
    assert actual_stack == expected_stack


async def verify_divide_command_failure(exception, initial_stack):
    with pytest.raises(exception):
        await verify_divide_command(
            DivideCommand(), RpnStack(elements=(1, 1, 1, 1, 1)), initial_stack
        )
