from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import csv


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


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







def wczytaj_plik(plik, klasa):
    lista=[]
    with open(plik, mode = "r", encoding="utf-8") as file:
        plik_CSV = csv.DictReader(file)
        for i in plik_CSV:
            # film = klasa(i["movieId"], i["title"], i["genres"])
            film = klasa(**i)
            lista.append(film)
    return lista

lista_filmow = wczytaj_plik("movies.csv", Movie)

lista_tagow = wczytaj_plik("tags.csv", Tag)

lista_ratingow = wczytaj_plik("ratings.csv", Rating)

lista_linkow = wczytaj_plik("links.csv", Link)




