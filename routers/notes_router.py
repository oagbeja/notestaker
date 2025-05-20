from fastapi import APIRouter,Depends
from models import auth_model
from services import auth_service
from database.initiate import get_db  # Your async session dependency
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

# TODO:
# Note comprises of: timestamp, details , categories[Enum] 


# Get All notes
#Get a particular note
#  Create a note
#  Update a note
#  Delete a note
