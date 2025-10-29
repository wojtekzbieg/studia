from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Numeric

import csv


app = FastAPI()

engine = create_engine("sqlite:///C:/Users/Wojtek/DataGripProjects/identifier.sqlite")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/filmy")
def wyswietl_filmy():
    return lista_filmow

@app.get("/tagi")
def wyswietl_tagi():
    return lista_tagow

@app.get("/ratingi")
def wyswietl_ratingi():
    return lista_ratingow

@app.get("/linki")
def wyswietl_linki():
    return lista_linkow


#   LISTA PYTHONOWA
# def wczytaj_plik(plik, klasa):
#     with open(plik, mode = "r", encoding="utf-8") as file:
#         plikCSV = csv.DictReader(file)
#         for i in plikCSV:
#             obiekt = klasa(**i)
#             # print(obiekt.title)
#             session.add(obiekt)


#   DATAFRAME
def wczytaj_plik(plik, klasa):
    df = pd.read_csv(plik)
    tuples = df.itertuples(index=False)
    for i in tuples:
        print(i)
        obiekt = klasa(**i._asdict())
        session.add(obiekt)



# lista_filmow = session.query(Movie).all()
# lista_tagow = session.query(Tag).all()
# lista_ratingow = session.query(Rating).all()
# lista_linkow = session.query(Link).all()


# wczytaj_plik("movies.csv", Movie)
# wczytaj_plik("tags.csv", Tag)
# wczytaj_plik("ratings.csv", Rating)
# wczytaj_plik("links.csv", Link)

# Base.metadata.create_all(engine)

# movie1 = Movie(movieId=1, title="Shrek", genres="Funny|Educational")

# session.add(movie1)
# session.query(Movie).delete()
session.commit()


# for i in movies:
#     print(i.movieId, i.title)

