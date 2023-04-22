# uvicorn main:app --reload
import os
from fastapi import FastAPI
from database.database import engine
from routers import anime
from database import models
from fastapi.middleware.cors import CORSMiddleware
from utils.api import origins

models.Base.metadata.create_all(bind=engine)
# APP
app = FastAPI()

app.include_router(anime.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello This is AnimAIxpert's API"}
