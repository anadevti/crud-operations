'''
modelagem dos dados
'''
from pydantic import BaseModel
from uuid import UUID, uuid4 # random id
from typing import Optional, List
from enum import Enum

class Role(str, Enum):
    role_admin = "admin"
    role_user = "aluna"
    role_prof = "professora"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    email: str
    role: List[Role]
