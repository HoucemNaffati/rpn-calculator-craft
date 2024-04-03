from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response
from pydantic import BaseModel

from rpn_calculator.shared.domain_types import CommandType
from rpn_calculator.write.core.usecases.append import (
    AppendCommand,
    AppendCommandHandler,
)
from rpn_calculator.write.web.configuration import get_append_command_handler


class AppendValueRequestParam(BaseModel):
    value: int


class ApplyCommandRequestParam(BaseModel):
    command: CommandType


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
    "/",
    status_code=201,
    description="Apply one of the calculator commands to the stack",
)
async def apply_command_to_the_stack(
    request_param: ApplyCommandRequestParam, request: Request, response: Response
):
    response.headers["Location"] = f"{request.url.path}"
