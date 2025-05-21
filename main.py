# main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from routers import auth_router,notes_router # Import your routers
import logging
from contextlib import asynccontextmanager
from database.create_tables import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()  # Run table creation on startup
    yield  # App runs here
    # Optional cleanup after shutdown
    
app = FastAPI(lifespan=lifespan)



@app.get("/")
def welcome():
    return {"message": "Welcome to Notetaker"}

app.include_router(auth_router.router, prefix="/auth",tags=['Authentication'])
app.include_router(notes_router.router, prefix="/notes",tags=['Note Taking'])
# app.include_router(users.router)

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error_"}
    )