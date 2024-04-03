from fastapi import APIRouter

from ....shared.domain_types import CommandType

router = APIRouter(prefix="/commands", tags=["Commands"])


@router.get("", description="Get all possible commands")
def list_commands():
    return CommandType.__members__
