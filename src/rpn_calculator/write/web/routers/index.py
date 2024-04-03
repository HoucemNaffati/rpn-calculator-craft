from fastapi import APIRouter

from . import stack

write_router = APIRouter(
    responses={
        "400": {"description": "Bad request"},
        "422": {"description": "Unprocessable entity: Domain logic exception"},
    }
)

write_router.include_router(stack.router)
