from typing import Union

from fastapi import FastAPI, Request, Response

from ...shared.web.global_exception_handlers import format_exception
from ..core.domain.exceptions import (
    CannotApplyRpnCommandException,
    DivisionByZeroException,
)


def __cannot_apply_rpn_command_exception_handler(
    _: Request, exception: Union[Exception, CannotApplyRpnCommandException]
) -> Response:
    return format_exception(exception, status=422)


def __division_by_zero_exception_handler(
    _: Request, exception: Union[Exception, DivisionByZeroException]
) -> Response:
    return format_exception(exception, status=422)


def add_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        CannotApplyRpnCommandException, __cannot_apply_rpn_command_exception_handler
    )
    app.add_exception_handler(
        DivisionByZeroException, __division_by_zero_exception_handler
    )
