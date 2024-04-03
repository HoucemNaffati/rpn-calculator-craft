from fastapi import APIRouter, Request, Response
from pydantic import BaseModel

from rpn_calculator.shared.domain_types import CommandType
from rpn_calculator.write.core.usecases.append import (
    AppendCommand,
    AppendCommandHandler,
)


class AppendValueRequestParam(BaseModel):
    value: int


class ApplyCommandRequestParam(BaseModel):
    command: CommandType


router = APIRouter(prefix="/stack", tags=["Stack"])


@router.post("/values", status_code=201, description="append a new value to the stack")
async def append_one_value_to_the_stack(
    request_param: AppendValueRequestParam, request: Request, response: Response
):
    command = AppendCommand(value=request_param.value)
    use_case = AppendCommandHandler()
    await use_case.handle(command)
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
