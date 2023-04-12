from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, ARRAY
from .database import Base

class Anime(Base):
    __annotations__ = "animes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    score = Column(Float)
    genres = Column(ARRAY(String))
    english_name = Column(String(255))
    japanese_name = Column(String(255))
    type = Column(String(255))
    episodes = Column(Integer)
    aired = Column(String(255))
    premiered = Column(String(255))

