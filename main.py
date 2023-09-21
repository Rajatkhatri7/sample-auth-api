from fastapi import FastAPI
from core.settings import settings
import schema
from routes import users_router
from database import engine,get_db

app = FastAPI()
schema.Base.metadata.create_all(bind=engine)

app.include_router(users_router)

@app.get("/")
def home():
    return {'status':"ok"}