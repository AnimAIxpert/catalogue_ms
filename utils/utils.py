from schemas.animes import Anime as AnimeSchema
from schemas.animes import AnimeAll as AnimeSchemaComplete
from database.models import Anime as AnimeModel

def process_char_list(x: list) -> list:
    return list(map(str.strip, "".join(x).split(",")))

def map_model_to_schema(anime_model: AnimeModel) -> AnimeSchema:
    anime_schema = AnimeSchema(
        id=anime_model.id,
        name=anime_model.name,
        image_url=anime_model.image_url
    )
    return anime_schema

def map_all_model_to_schema(anime_model: AnimeModel) -> AnimeSchemaComplete:
    anime_schema = AnimeSchemaComplete(
        id=anime_model.id,
        name=anime_model.name,
        score=anime_model.score,
        genres = process_char_list(anime_model.genres),
        english_name=anime_model.english_name,
        japanese_name=anime_model.japanese_name,
        type=anime_model.type,
        episodes=anime_model.episodes,
        aired=anime_model.aired,
        premiered=anime_model.premiered,
        producers = process_char_list(anime_model.producers),
        licensors = process_char_list(anime_model.licensors),
        studios = process_char_list(anime_model.studios),
        source=anime_model.source,
        duration=anime_model.duration,
        audience=anime_model.audience,
        synopsis=anime_model.synopsis,
        image_url=anime_model.image_url
    )
    
    return anime_schema