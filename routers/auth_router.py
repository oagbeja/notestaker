from fastapi import APIRouter
from models import auth_model
from services import auth_service

router = APIRouter()


@router.post("/")
def login(user_item:auth_model.UserBody):
    return auth_service.login(user_item)
    