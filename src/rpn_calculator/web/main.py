from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from ..read.web.routers.index import read_router
from ..shared.web.global_exception_handlers import http_validation_exception_handler
from ..write.web.exception_handlers import add_exception_handlers
from ..write.web.routers.index import write_router


def build_fast_api_app() -> FastAPI:
    api = FastAPI(
        root_path="/rpn_calculator/v1",
        title="RPN Calculator",
        description="Reverse Polish Notation (RPN) calculator API",
    )
    # shared
    api.add_exception_handler(RequestValidationError, http_validation_exception_handler)

    # read
    api.include_router(read_router)

    # write
    api.include_router(write_router)
    add_exception_handlers(api)
    return api


app = build_fast_api_app()
