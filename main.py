from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel
from database import engineconn
from models import Test

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()

class Item(BaseModel):
    name: str
    number: int

@app.get("/")
async def root():
    example = session.query(Test).all()
    return example


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
