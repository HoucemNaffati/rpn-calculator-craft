from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from rpn_calculator.read.web.routers.index import read_router
from rpn_calculator.shared.web.global_exception_handlers import (
    http_validation_exception_handler,
)
from rpn_calculator.write.web.routers.index import write_router

app = FastAPI(
    root_path="/rpn_calculator/v1",
    title="RPN Calculator",
    description="Reverse Polish Notation (RPN) calculator API",
)


# shared
app.add_exception_handler(RequestValidationError, http_validation_exception_handler)

# read
app.include_router(read_router)

# write
app.include_router(write_router)
