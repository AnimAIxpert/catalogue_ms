from sqlalchemy.orm import Session
from schemas import animes
from database.models import Anime

def get_Anime(db: Session, anime_id: int):
    return db.query(Anime).filter(Anime.id == anime_id).first()

def get_animes_by_genre(db: Session, genre: str, limit: int = 100):
    return db.query(Anime).filter(Anime.genres.contains(genre)).all()

def get_animes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Anime).offset(skip).limit(limit).all()


def create_anime(db: Session, anime: animes.Anime):
    db_anime = Anime(
        id=anime.id,
        name=anime.name,
        score=anime.score,
        genres=anime.genres,
        english_name=anime.english_name,
        japanese_name=anime.japanese_name,
        type=anime.type,
        episodes=anime.episodes,
        aired=anime.aired,
        premiered=anime.premiered,
        producers=anime.producers,
        licensors=anime.licensors,
        studios=anime.studios,
        source=anime.source,
        duration=anime.duration,
        audience=anime.audience
    )
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return db_anime

def update_anime(db: Session, anime: animes.Anime):
    db_anime = db.query(Anime).filter(Anime.id == anime.id).first()
    diff = {}
    if anime.name != db_anime.name:
        diff[Anime.name] = anime.name
    if anime.score != db_anime.score:
        diff[Anime.score] = anime.score
    if anime.genres != db_anime.genres:
        diff[Anime.genres] = anime.genres
    if anime.english_name != db_anime.english_name:
        diff[Anime.english_name] = anime.english_name
    if anime.japanese_name != db_anime.japanese_name:
        diff[Anime.japanese_name] = anime.japanese_name
    if anime.type != db_anime.type:
        diff[Anime.type] = anime.type
    if anime.episodes != db_anime.episodes:
        diff[Anime.episodes] = anime.episodes
    if anime.aired != db_anime.aired:
        diff[Anime.aired] = anime.aired
    if anime.premiered != db_anime.premiered:
        diff[Anime.premiered] = anime.premiered
    if anime.producers != db_anime.producers:
        diff[Anime.producers] = anime.producers
    if anime.licensors != db_anime.licensors:
        diff[Anime.licensors] = anime.licensors
    if anime.studios != db_anime.studios:
        diff[Anime.studios] = anime.studios
    if anime.source != db_anime.source:
        diff[Anime.source] = anime.source
    if anime.duration != db_anime.duration:
        diff[Anime.duration] = anime.duration
    if anime.audience != db_anime.audience:
        diff[Anime.audience] = anime.audience

    if diff: db.query(Anime).filter(Anime.id == anime.id).update(diff, synchronize_session=False)
    db.commit()
    db.refresh(db_anime)
    return db_anime

