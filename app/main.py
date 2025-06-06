from fastapi import FastAPI, Header
import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User
from schemas import UserCreate, UserOut


app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Бомби Слава"}

@app.post("/agen")
def create_agen(user_agent: str = Header(str)):
    return user_agent




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
