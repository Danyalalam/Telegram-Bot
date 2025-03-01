from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.models import SessionLocal, User, Conversation

app = FastAPI(title="Feng Shui Bot API")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Feng Shui Bot API is running"}

@app.get("/users/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.get("/conversations/")
async def get_conversations(user_id: int = None, db: Session = Depends(get_db)):
    if user_id:
        conversations = db.query(Conversation).filter(Conversation.user_id == user_id).all()
    else:
        conversations = db.query(Conversation).all()
    return conversations