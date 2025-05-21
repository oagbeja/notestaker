from pydantic import BaseModel
from enum import Enum
from typing import Optional


class Categories(str, Enum):
    default = "default"
    house = "house"
    work = "work"
    entertainment = "entertainment"
    
class NoteBody(BaseModel):
    title:str | None =None
    details: str
    category: Categories | None =None

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    details: Optional[str] = None
    category: Optional[Categories] = None

