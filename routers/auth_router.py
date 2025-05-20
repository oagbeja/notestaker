from fastapi import APIRouter,Depends
from models import auth_model
from services import auth_service
from database.initiate import get_db  # Your async session dependency
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.post("/")
async def login(user_item:auth_model.UserBody, db: AsyncSession = Depends(get_db)):
    return await auth_service.login(db,user_item)
    
@router.post("/register")
async def login(user_item:auth_model.UserBodyCreate, db: AsyncSession = Depends(get_db)):    
    return await auth_service.create_new_user(db,user_item)