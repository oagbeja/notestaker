from typing import Union

from fastapi import FastAPI

app = FastAPI()

users = [{"username":'ade',"password":'123456'}]

@app.get("/")
def welcome():
    return {"message": "Welcome to Notetaker"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}