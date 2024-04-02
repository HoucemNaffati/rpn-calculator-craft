from fastapi import APIRouter

from rpn_calculator.write.web.routers import stack

write_router = APIRouter(
    responses={
        "400": {"description": "Bad request"},
        "422": {"description": "Unprocessable entity: Domain logic exception"},
    }
)

write_router.include_router(stack.router)
