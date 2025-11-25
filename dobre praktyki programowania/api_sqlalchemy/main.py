from typing import Annotated
from connection import session
from models import Item, Movie, Tag, Rating, Link, User
from fastapi import FastAPI, Body, HTTPException, status, Header
# import csv
import jwt
from datetime import datetime, timedelta, timezone
from load_data import dodaj_uzytkownika, zaloguj_uzytkownika



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


@app.post("/rejestracja")
def rejestracja(email: str = Body(), haslo: str = Body()):
    try:
        user = dodaj_uzytkownika(email, haslo)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    except TypeError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return f"{user.email}, {user.userId}, Użytkownik zarejestrowany pomyślnie."


@app.post("/logowanie")
def login(email: str = Body(), haslo: str = Body()):
    try:
        user, token = zaloguj_uzytkownika(email, haslo)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    return {"token": token, "token_type": "bearer"}


klucz="asnfj46fsdvtd5fg"
algorytm="HS256"
defaultowy_czas_waznosci_tokenu = 30


def stworz_token(payload: dict, czas_waznosci_tokenu: int | None = None):
    if czas_waznosci_tokenu is None:
        czas_waznosci_tokenu = defaultowy_czas_waznosci_tokenu

    exp = datetime.now(timezone.utc) + timedelta(minutes=czas_waznosci_tokenu)
    payload.update({"exp": exp})

    JWT_token_encoded = jwt.encode(payload=payload, key=klucz, algorithm=algorytm)
    return JWT_token_encoded


def zdekoduj_token(token):
    JWT_token_decoded = jwt.decode(jwt=token, key=klucz, algorithms=[algorytm])
    return JWT_token_decoded


# token = stworz_token({"sub": "testowy_user"})
# print(token)
# print(zdekoduj_token(token))


# print(dodaj_uzytkownika("asdfghjkl@gmail.com", "haslohaslo123"))


def wyciagnij_token(authorization: str = Header(default=None)):
    if authorization is None:
        raise ValueError("Brak nagłówka Authorization")

    pociety_naglowek = authorization.split(" ")

    if len(pociety_naglowek) != 2 or pociety_naglowek[0].lower() != "bearer":
        raise ValueError("Niepoprawny format nagłówka Authorization")

    token = pociety_naglowek[-1]
    return token


def sprawdz_token():
    try:
        token = wyciagnij_token()
        zdekodowany_token = zdekoduj_token(token)
        return zdekodowany_token.get("sub")
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token wygasł")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Niepoprawny token")


# print(sprawdz_token("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0b3d5X3VzZXIiLCJleHAiOjE3NjQwODM1NDN9.VMOIbsULjjpyKq2aYXo9C6U6HZOhnJuuh4nuW-P0gkA"))