from pydantic import BaseModel

from ....shared.domain_types import CommandType


class AppendValueRequestParam(BaseModel):
    value: float


class ApplyCommandRequestParam(BaseModel):
    command: CommandType
