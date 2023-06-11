from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from .database import Base

# Base = declarative_base()

class Anime(Base):
    __tablename__ = "animes"
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
    producers = Column(ARRAY(String))
    licensors = Column(ARRAY(String))
    studios = Column(ARRAY(String))
    source = Column(String(255))
    duration = Column(String(255))
    audience = Column(String(255))
    synopsis = Column(Text())
    image_url = Column(String(255))

