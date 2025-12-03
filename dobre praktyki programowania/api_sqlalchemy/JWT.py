from datetime import datetime, timedelta, timezone
import jwt
from fastapi import Header, HTTPException, status
import bcrypt
from models import User
import os
from dotenv import load_dotenv

load_dotenv()

klucz = os.getenv("KLUCZ")
algorytm = os.getenv("ALGORYTM")
defaultowy_czas_waznosci_tokenu = int(os.getenv("DEFAULTOWY_CZAS_WAZNOSCI_TOKENU"))


def stworz_token(payload: dict, czas_waznosci_tokenu: int | None = None):
    if czas_waznosci_tokenu is None:
        czas_waznosci_tokenu = defaultowy_czas_waznosci_tokenu

    exp = datetime.now(timezone.utc) + timedelta(minutes=czas_waznosci_tokenu)
    payload.update({"exp": exp})

    JWT_token_encoded = jwt.encode(payload=payload, key=klucz, algorithm=algorytm)
    return JWT_token_encoded


def zdekoduj_token(token):    # -> payload
    JWT_token_decoded = jwt.decode(jwt=token, key=klucz, algorithms=[algorytm])
    return JWT_token_decoded


def wyciagnij_token(authorization):
    if authorization is None:
        raise ValueError("Brak nagłówka Authorization")
    print(authorization)
    pociety_naglowek = authorization.split(" ")

    if len(pociety_naglowek) != 2 or pociety_naglowek[0].lower() != "bearer":
        raise ValueError("Niepoprawny format nagłówka Authorization")

    token = pociety_naglowek[-1]
    return token


def sprawdz_token(authorization: str = Header(default=None)):
    try:
        token = wyciagnij_token(authorization)
        zdekodowany_token = zdekoduj_token(token)
        return zdekodowany_token
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token wygasł")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Niepoprawny token")



def zaloguj_uzytkownika(email, haslo, session):
    user = session.query(User).filter(User.email == email).first()

    if not user:
        raise ValueError("Niepoprawny email lub hasło.")

    haslo_bajty = haslo.encode("utf-8")
    zahashowane_haslo_bajty = user.hashed_password.encode("utf-8")

    if not bcrypt.checkpw(haslo_bajty, zahashowane_haslo_bajty):
        raise ValueError("Niepoprawny email lub hasło.")

    token = stworz_token(payload={"sub": user.email, "is_admin": user.is_admin})
    return user, token


def zarejestruj_uzytkownika(email, haslo, session):
    if session.query(User).filter(User.email == email).first():
        raise ValueError("Użytkownik o podanym emailu już istnieje.")

    if "@" not in email or "." not in email:
        raise TypeError("Niepoprawny email.")
    if len(haslo) < 8:
        raise TypeError("Hasło musi mieć co najmniej 8 znaków.")

    haslo_bajty = haslo.encode("utf-8")
    sol = bcrypt.gensalt()
    zahashowane_haslo = bcrypt.hashpw(haslo_bajty, sol).decode("utf-8")

    user = User(email=email, hashed_password=zahashowane_haslo, is_admin=0)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user



# testowyuser@gmail.com, haslohaslo123
# jankowalski@gmail.com, qwerty123
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqYW5rb3dhbHNraUBnbWFpbC5jb20iLCJleHAiOjE3NjQxNDQzNDJ9.u00sIuom4Ux8Tqt9Lou3kH91YOovkk-ddYIl_HzjL9o
# token = stworz_token({"sub": "testowyuser@gmail.com", "is_admin": 0})
# print(token)
# print(zdekoduj_token(token))


# print(dodaj_uzytkownika("asdfghjkl@gmail.com", "haslohaslo123"))


# print(sprawdz_token("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0b3d5X3VzZXIiLCJleHAiOjE3NjQwODM1NDN9.VMOIbsULjjpyKq2aYXo9C6U6HZOhnJuuh4nuW-P0gkA"))






