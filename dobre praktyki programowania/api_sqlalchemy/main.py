from typing import Union
from fastapi import FastAPI
from connection import session
from models import Item, Movie, Tag, Rating, Link
# import csv


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/filmy")
def wyswietl_filmy():
    lista_filmow = session.query(Movie).all()
    return lista_filmow


@app.get("/tagi")
def wyswietl_tagi():
    lista_tagow = session.query(Tag).all()
    return lista_tagow


@app.get("/ratingi")
def wyswietl_ratingi():
    lista_ratingow = session.query(Rating).all()
    return lista_ratingow


@app.get("/linki")
def wyswietl_linki():
    lista_linkow = session.query(Link).all()
    return lista_linkow


