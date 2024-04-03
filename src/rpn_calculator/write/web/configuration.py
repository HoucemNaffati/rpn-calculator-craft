from ..adapters.configuration import get_stack_repository
from ..core.usecases.add import AddCommandHandler
from ..core.usecases.append import AppendCommandHandler


def get_append_command_handler():
    return AppendCommandHandler(get_stack_repository())


def get_add_command_handler():
    return AddCommandHandler(get_stack_repository())
