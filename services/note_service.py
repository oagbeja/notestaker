from models.note_model import NoteBody
from database.note_schema import Note
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select,update,delete

from datetime import datetime

async def create_new_note(db: AsyncSession,note:NoteBody,user_id:int|str):
    try:
        db_note = Note(**note.model_dump())
        db_note.user_id = user_id
        db.add(db_note)
        await db.commit()
        await db.refresh(db_note)
        return {
            "data":db_note,
            "message":"Note successfully created"
        }
        
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )


async def update_note(db: AsyncSession,note:NoteBody,note_id:int|str):
    try:
        # db_note = Note(**note.model_dump(exclude_unset=True))

        stmt = (
            update(Note)
            .where(Note.id == note_id)
            .values(**note.model_dump(exclude_unset=True),updated_at=datetime.utcnow())
            .execution_options(synchronize_session="fetch")
        )

        await db.execute(stmt)
        await db.commit()
         # Optionally fetch updated note
        result = await db.execute(select(Note).where(Note.id == note_id))
        updated_note = result.scalar_one_or_none()

        # return updated_note
        return {
            "data":updated_note,
            "message":"Note successfully updated"
        }
        
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )


async def delete_note(db: AsyncSession,note_id:int|str):
    try:
       
        stmt = delete(Note).where(Note.id == note_id)
        result = await db.execute(stmt)
        await db.commit()

        if result.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Note not found "
            )

        return {"message": "Note deleted successfully"}
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

async def get_note_by_id(db: AsyncSession,note_id:int|str):
    try:
        # db_note = Note(**note.model_dump(exclude_unset=True))
        result = await db.execute(select(Note).where(
            (Note.id == note_id) 
        ))
        
        note = result.scalars().first()      
       
        return {
            "data":note,
            "message":"Note successfully fetched"
        }        
         
        
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

async def get_notes_by_user(db: AsyncSession,user_id:int|str):
    try:
        # db_note = Note(**note.model_dump(exclude_unset=True))
        result = await db.execute(select(Note).where(
            (Note.user_id == user_id) 
        ))
        
        notes = result.scalars().all()     
       
        return {
            "data":notes,
            "message":"Note successfully fetched"
        }        
         
        
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )
