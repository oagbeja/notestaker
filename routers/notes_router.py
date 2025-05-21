from fastapi import APIRouter,Depends,HTTPException, status
from models.note_model import NoteBody
from services import note_service
from database.initiate import get_db  # Your async session dependency
from sqlalchemy.ext.asyncio import AsyncSession
from utils.token import bearer_scheme
from utils.jwt import get_user_payload



router = APIRouter()

# TODO:
# Note comprises of: timestamp, details ,title, category[Enum] 


# Get All notes
@router.get("/")
async def get_notes_by_user( db: AsyncSession = Depends(get_db),token: str = Depends(bearer_scheme)):    
    tokenPayload = get_user_payload(token)    
    return await note_service.get_notes_by_user(db,tokenPayload["id"])


#Get a particular note
@router.get("/{note_id}")
async def get_note_by_id( note_id:str|int,db: AsyncSession = Depends(get_db),token: str = Depends(bearer_scheme)):    
    get_user_payload(token)    
    return await note_service.get_note_by_id(db,note_id)


#  Create a note
@router.post("/")
async def create_new_note( note:NoteBody,db: AsyncSession = Depends(get_db),token: str = Depends(bearer_scheme)):    
    tokenPayload =   get_user_payload(token)    
    return await note_service.create_new_note(db,note,tokenPayload["id"])

#  Update a note
@router.put("/{note_id}")
async def update_note( note:NoteBody,note_id:str|int,db: AsyncSession = Depends(get_db),token: str = Depends(bearer_scheme)):    
    get_user_payload(token)    
    return await note_service.update_note(db,note,note_id)

#  Delete a note
@router.delete("/{note_id}")
async def update_note( note_id:str|int,db: AsyncSession = Depends(get_db),token: str = Depends(bearer_scheme)):    
    get_user_payload(token)    
    return await note_service.delete_note(db,note_id)
