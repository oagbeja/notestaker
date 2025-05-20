from models import auth_model
from database.user_schema import User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from utils.hash import hash_password,verify_password
from utils.jwt import create_access_token


async def create_new_user(db: AsyncSession,user:auth_model.UserBodyCreate):
    try:
        db_user = User(**user.model_dump())
        # check if a user exist:
        result = await db.execute(select(User).where(
            (User.email == user.email) 
        ))
        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists"
            )
        db_user.password = hash_password(db_user.password)
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
       
        return {"result":{
            "name":db_user.name,
            "email":db_user.email,
            "id":db_user.id,
            "token": create_access_token({"name":db_user.name,
                "email":db_user.email,
                "id":db_user.id
                })
        }}
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

async def login(db: AsyncSession,user_item:auth_model.UserBody):    
    try:
        result = await db.execute(select(User).where(
                (User.email == user_item.email) 
            ))
        existing_user = result.scalars().first()
        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
        if not verify_password(user_item.password,existing_user.password):
             raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid password"
            )
            
        return {"result":{
            "name":existing_user.name,
            "email":existing_user.email,
            "id":existing_user.id,
            "token": create_access_token({"name":existing_user.name,
                "email":existing_user.email,
                "id":existing_user.id
                })
        }}
    
    except Exception as e:        
        raise HTTPException(
            status_code= e.status_code or status.HTTP_400_BAD_REQUEST,
            detail=e.detail or f"Database error: {str(e)}"
        )