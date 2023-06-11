from fastapi import APIRouter
import pandas as pd
from database.database import SessionLocal
from database.models import Anime
from database.crud import get_Anime
from utils.utils import map_model_to_schema, map_all_model_to_schema
from database.load_database import load_base_data, load_sypnosis, load_images_path

db_session = SessionLocal()

router = APIRouter()

# @router.get("/anime")
# async def get_animeid(id: int):

@router.get("/read_anime_database")
async def update_anime_database():
    ans = ""
    if not load_base_data():
        ans += "error loading base data \n "
    else:
        ans += "success loading base data \n "
    if not load_sypnosis():
        ans += "error loading sypnosis \n "
    else:
        ans += "success loading sypnosis \n "
    if not load_images_path():
        ans += "error loading image urls \n "
    else:
        ans += "success loading image urls \n "
    return ans


@router.get("/anime")
async def get_anime(id: int):
    anime = get_Anime(db_session, id)
    return map_all_model_to_schema(anime)

@router.get("/anime-by-genre")
async def get_animes(genre: str, limit: int | None = None):
    animes = db_session.query(Anime).filter(Anime.genres.contains(list(genre))).limit(limit).all()
    return list(map(map_model_to_schema, animes))

@router.get("/anime-top")
async def get_animes_top(limit: int | None = None, genre: str | None = None):
    if genre is None:
        animes = db_session.query(Anime).order_by(Anime.score.desc()).limit(limit).all()
    else:
        animes = db_session.query(Anime).filter(Anime.genres.contains(list(genre))).order_by(Anime.score.desc()).limit(limit).all()
    return list(map(map_model_to_schema, animes))