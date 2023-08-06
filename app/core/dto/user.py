from dataclasses import dataclass
from datetime import datetime as dt

from app.core.enums import RolesType


@dataclass(frozen=True)
class UserDTO:
    id: int
    tid: int
    cid: int
    language: str
    role: RolesType
    datetime: dt
