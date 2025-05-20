# main.py
from fastapi import FastAPI
from routers import auth_router  # Import your routers

app = FastAPI()

app.include_router(auth_router.router, prefix="/auth")
# app.include_router(users.router)

@app.get("/")
def welcome():
    return {"message": "Welcome to Notetaker"}