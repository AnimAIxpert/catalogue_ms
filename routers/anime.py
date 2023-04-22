from fastapi import APIRouter
import pandas as pd
from database.database import SessionLocal
from database.models import Anime
from database.crud import get_Anime
from utils.utils import map_model_to_schema

db_session = SessionLocal()


router = APIRouter()

# @router.get("/anime")
# async def get_animeid(id: int):

@router.get("/read_anime_database")
async def update_anime_database():
    data = pd.read_csv("data/anime.csv")
    # print(data)
    # anime = data.iloc[0]
    for ind, anime in data.iterrows():
        temp = Anime()
        if anime["MAL_ID"] != "Unknown":
            temp.id = anime["MAL_ID"]
        temp.name = anime["Name"]
        if anime["Score"] == "Unknown":
            temp.score = 0
        else: 
            temp.score = anime["Score"]
        temp.genres = anime["Genres"]
        temp.english_name = anime["English name"]
        temp.japanese_name = anime["Japanese name"]
        temp.type = anime["Type"]
        if anime["Episodes"] == "Unknown":
            temp.episodes = 0
        else:
            temp.episodes = anime["Episodes"]
        temp.aired = anime["Aired"]
        temp.premiered = anime["Premiered"]
        temp.producers = anime["Producers"]
        temp.licensors = anime["Licensors"]
        temp.studios = anime["Studios"]
        temp.source = anime["Source"]
        temp.duration = anime["Duration"]
        temp.audience = anime["Rating"]
        db_session.add(temp)
    db_session.commit()
    return "database updated"

@router.get("/anime")
async def get_anime(id: int):
    anime = get_Anime(db_session, id)
    return map_model_to_schema(anime)

@router.get("/anime-by-genre")
async def get_animes(genre: str, limit: int | None = None):
    animes = db_session.query(Anime).filter(Anime.genres.contains(list(genre))).limit(limit).all()
    return list(map(map_model_to_schema, animes))
