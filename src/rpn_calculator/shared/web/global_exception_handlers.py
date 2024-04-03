from typing import Union

from fastapi import Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def http_validation_exception_handler(
    _: Request, exception: Union[Exception, RequestValidationError]
) -> Response:
    return format_exception(exception, status=400)


def format_exception(exception, status):
    return JSONResponse(
        status_code=status,
        content={"name": exception.__class__.__name__, "detail": str(exception)},
    )
