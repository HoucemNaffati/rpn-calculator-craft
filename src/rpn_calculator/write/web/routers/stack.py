from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response

from ....shared.domain_types import CommandType
from ...core.usecases.add import AddCommand, AddCommandHandler
from ...core.usecases.append import AppendCommand, AppendCommandHandler
from ...core.usecases.clear import ClearCommand, ClearCommandHandler
from ...core.usecases.divide import DivideCommand, DivideCommandHandler
from ...core.usecases.multiply import MultiplyCommand, MultiplyCommandHandler
from ...core.usecases.subtract import SubtractCommand, SubtractCommandHandler
from ..configuration import (
    get_add_command_handler,
    get_append_command_handler,
    get_clear_command_handler,
    get_divide_command_handler,
    get_multiply_command_handler,
    get_subtract_command_handler,
)
from .request_params import AppendValueRequestParam, ApplyCommandRequestParam

router = APIRouter(prefix="/stack", tags=["Stack"])


@router.post("/values", status_code=201, description="append a new value to the stack")
async def append_one_value_to_the_stack(
    request_param: AppendValueRequestParam,
    request: Request,
    response: Response,
    append_command_handler: Annotated[
        AppendCommandHandler, Depends(get_append_command_handler)
    ],
):
    await append_command_handler.handle(AppendCommand(value=request_param.value))
    response.headers["Location"] = f"{request.url.path}".replace("values", "")
    return {}


@router.put(
    "",
    status_code=201,
    description="Apply one of the calculator commands to the stack",
)
async def apply_command_to_the_stack(
    request_param: ApplyCommandRequestParam,
    request: Request,
    response: Response,
    add_command_handler: Annotated[AddCommandHandler, Depends(get_add_command_handler)],
    subtract_command_handler: Annotated[
        SubtractCommandHandler, Depends(get_subtract_command_handler)
    ],
    multiply_command_handler: Annotated[
        MultiplyCommandHandler, Depends(get_multiply_command_handler)
    ],
    divide_command_handler: Annotated[
        DivideCommandHandler, Depends(get_divide_command_handler)
    ],
    clear_command_handler: Annotated[
        ClearCommandHandler, Depends(get_clear_command_handler)
    ],
):
    print(request_param.command.value)
    match request_param.command.value:
        case CommandType.add:
            await add_command_handler.handle(AddCommand())
        case CommandType.subtract:
            await subtract_command_handler.handle(SubtractCommand())
        case CommandType.multiply:
            await multiply_command_handler.handle(MultiplyCommand())
        case CommandType.divide:
            await divide_command_handler.handle(DivideCommand())
        case CommandType.clear:
            await clear_command_handler.handle(ClearCommand())

    response.headers["Location"] = f"{request.url.path}"
    return {}
