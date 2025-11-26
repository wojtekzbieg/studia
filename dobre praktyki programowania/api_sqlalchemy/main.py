from connection import session
from models import Item, Movie, Tag, Rating, Link
from fastapi import FastAPI, Body, HTTPException, status, Depends
from JWT import sprawdz_token, zarejestruj_uzytkownika, zaloguj_uzytkownika



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
def wyswietl_filmy(payload: str = Depends(sprawdz_token)):
    lista_filmow = session.query(Movie).all()
    return {"user": payload, "filmy": lista_filmow}


@app.get("/tagi")
def wyswietl_tagi(payload: str = Depends(sprawdz_token)):
    lista_tagow = session.query(Tag).all()
    return {"user": payload, "tagi": lista_tagow}


@app.get("/ratingi")
def wyswietl_ratingi(payload: str = Depends(sprawdz_token)):
    lista_ratingow = session.query(Rating).all()
    return {"user": payload, "ratingi": lista_ratingow}


@app.get("/linki")
def wyswietl_linki(payload: str = Depends(sprawdz_token)):
    lista_linkow = session.query(Link).all()
    return {"user": payload, "linki": lista_linkow}


@app.get("/user-details")
def szczegoly_uzytkownika(payload: str = Depends(sprawdz_token)):
    return payload


@app.post("/rejestracja")
def rejestracja(email: str = Body(), haslo: str = Body()):
    try:
        user = zarejestruj_uzytkownika(email, haslo)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    except TypeError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return f"{user.email}, {user.userId}, {user.is_admin}, Użytkownik zarejestrowany pomyślnie."


@app.post("/logowanie")
def login(email: str = Body(), haslo: str = Body()):
    try:
        user, token = zaloguj_uzytkownika(email, haslo)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    return {"token": token, "token_type": "bearer"}


