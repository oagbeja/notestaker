from pydantic import BaseModel, EmailStr

class UserBody(BaseModel):
    email: str
    password: str

class UserBodyCreate(BaseModel):
    name: str
    password: str
    email: EmailStr


