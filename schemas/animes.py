from pydantic import BaseModel


class Anime(BaseModel):
    id: int
    name: str
    image_url: str | None
    
class AnimeAll(Anime):
    score: float
    genres: list
    english_name: str
    japanese_name: str
    type: str
    episodes: int
    aired: str
    premiered: str
    producers: list
    licensors: list
    studios: list
    source: str
    duration: str
    audience: str
    synopsis: str | None
    
    