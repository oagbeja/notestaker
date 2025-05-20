from pydantic import BaseModel

class UserBody(BaseModel):
    name: str
    password: str