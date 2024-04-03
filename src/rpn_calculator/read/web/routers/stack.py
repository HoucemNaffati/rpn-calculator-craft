from fastapi import APIRouter

from src.rpn_calculator.shared.stack_database import database

router = APIRouter(prefix="/stack", tags=["Stack"])


@router.get("", description="Get the current stack state")
def display_last_stack_state():
    return database
