from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Numeric, Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


class Movie(Base):
    __tablename__ = "Movies"

    movieId = Column(Integer, primary_key=True)
    title = Column(String(100))
    genres = Column(String(100))


class Tag(Base):
    __tablename__ = "Tags"

    tagId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer)
    movieId = Column(Integer)
    tag = Column(String(50))
    timestamp = Column(Integer)


class Rating(Base):
    __tablename__ = "Ratings"

    ratingId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer)
    movieId = Column(Integer)
    rating = Column(Numeric(2, 1))
    timestamp = Column(Integer)


class Link(Base):
    __tablename__ = "Links"

    movieId = Column(Integer, primary_key=True)
    imdbId = Column(Integer)
    tmdbId = Column(Integer)


class User(Base):
    __tablename__ = "Users"

    userId = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100))
    hashed_password = Column(String(200))
    is_admin = Column(Integer, default=0)


class ImageAnalysisResult(Base):
    __tablename__ = "ImageAnalysisResults"

    id = Column(Integer, primary_key=True, autoincrement=True)
    worker_task_id = Column(Integer, unique=True)
    img_url = Column(String(200))
    people_count = Column(Integer)
    processing_time = Column(Float)
