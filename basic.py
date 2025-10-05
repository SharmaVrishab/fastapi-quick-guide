# main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    email: str


@app.get("/")
def read_root():
    return JSONResponse(content={"message": "this is root"})


@app.get("/users")
def get_users(limit: int = 10):
    return {"limit": limit}


@app.post("/users")
def create_user(user: User):
    return {"user": user}
