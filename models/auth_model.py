from pydantic import BaseModel, EmailStr

class UserBody(BaseModel):
    email: EmailStr
    password: str

class UserBodyCreate(BaseModel):
    name: str
    password: str
    email: EmailStr


