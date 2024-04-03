from fastapi import APIRouter

from . import commands, stack

read_router = APIRouter(
    responses={"400": {"description": "Bad request"}},
)

read_router.include_router(commands.router)
read_router.include_router(stack.router)
