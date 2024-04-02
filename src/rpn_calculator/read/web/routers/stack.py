from fastapi import APIRouter

router = APIRouter(prefix="/stack", tags=["Stack"])


@router.get("/", description="Get the current stack state")
def display_last_stack_state():
    return {"stack": "[]"}
