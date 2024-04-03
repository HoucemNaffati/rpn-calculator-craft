from rpn_calculator.write.adapters.configuration import get_stack_repository
from rpn_calculator.write.core.usecases.append import AppendCommandHandler


def get_append_command_handler():
    return AppendCommandHandler(get_stack_repository())
