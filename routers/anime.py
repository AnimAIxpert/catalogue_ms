from fastapi import APIRouter
import pandas as pd
from database.database import SessionLocal

db_session = SessionLocal()


router = APIRouter()

# @router.get("/anime")
# async def get_animeid(id: int):

@router.get("/update_anime_database")
async def update_anime_database():
    data = pd.read_csv("data/anime.csv")
    print(data)
    return "xd"
    
