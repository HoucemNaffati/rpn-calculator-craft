from ..adapters.configuration import get_stack_repository
from ..core.usecases.add import AddCommandHandler
from ..core.usecases.append import AppendCommandHandler
from ..core.usecases.divide import DivideCommandHandler
from ..core.usecases.multiply import MultiplyCommandHandler
from ..core.usecases.subtract import SubtractCommandHandler


def get_append_command_handler():
    return AppendCommandHandler(get_stack_repository())


def get_add_command_handler():
    return AddCommandHandler(get_stack_repository())


def get_subtract_command_handler():
    return SubtractCommandHandler(get_stack_repository())


def get_multiply_command_handler():
    return MultiplyCommandHandler(get_stack_repository())


def get_divide_command_handler():
    return DivideCommandHandler(get_stack_repository())
