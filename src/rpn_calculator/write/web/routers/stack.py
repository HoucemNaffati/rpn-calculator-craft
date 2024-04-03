from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status

from ....shared.domain_types import CommandType
from ...core.usecases.add import AddCommand, AddCommandHandler
from ...core.usecases.append import AppendCommand, AppendCommandHandler
from ...core.usecases.subtract import SubtractCommand, SubtractCommandHandler
from ..configuration import (
    get_add_command_handler,
    get_append_command_handler,
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
):
    print(request_param.command.value)
    match request_param.command.value:
        case CommandType.add:
            await add_command_handler.handle(AddCommand())
        case CommandType.subtract:
            await subtract_command_handler.handle(SubtractCommand())
        case _:
            raise HTTPException(
                status_code=status.HTTP_501_NOT_IMPLEMENTED,
                detail="unsupported command",
            )

    response.headers["Location"] = f"{request.url.path}"
    return {}
