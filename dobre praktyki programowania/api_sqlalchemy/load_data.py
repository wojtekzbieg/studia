from sqlalchemy.orm import declarative_base
import pandas as pd
from connection import session, engine
from models import Movie, Tag, Rating, Link, User
import bcrypt
from main import stworz_token


Base = declarative_base()


#       WCZYTYWANIE PLIKOW DO BAZY - DATAFRAME
def wczytaj_plik(plik, klasa):
    df = pd.read_csv(plik)
    tuples = df.itertuples(index=False)
    for i in tuples:
        # print(i)
        obiekt = klasa(**i._asdict())
        session.add(obiekt)

#       WCZYTYWANIE PLIKOW DO BAZY - LISTA PYTHONOWA
# def wczytaj_plik(plik, klasa):
#     with open(plik, mode = "r", encoding="utf-8") as file:
#         plikCSV = csv.DictReader(file)
#         for i in plikCSV:
#             obiekt = klasa(**i)
#             # print(obiekt.title)
#             session.add(obiekt)


#       WCZYTYWANIE PLIKOW DO BAZY
# wczytaj_plik("data/movies.csv", Movie)
# wczytaj_plik("data/tags.csv", Tag)
# wczytaj_plik("data/ratings.csv", Rating)
# wczytaj_plik("data/links.csv", Link)

#       USUNIECIE ZAWARTOSCI TABELI
# session.query(Movie).delete()

#       DODAWANIE USERA
# user1 = User(email="xyz@gmail.com", hashed_password=get_password_hash("abcd1234"))
# session.add(user1)

#      COMMIT ZMIAN
# session.commit()

#      UTWORZENIE TABEL W BAZIE JESLI ICH NIE MA
# Base.metadata.create_all(engine)


def dodaj_uzytkownika(email, haslo):
    if session.query(User).filter(User.email == email).first():
        raise ValueError("Użytkownik o podanym emailu już istnieje.")

    if "@" not in email or "." not in email:
        raise TypeError("Niepoprawny email.")
    if len(haslo) < 8:
        raise TypeError("Hasło musi mieć co najmniej 8 znaków.")

    haslo_bajty = haslo.encode("utf-8")
    sol = bcrypt.gensalt()
    zahashowane_haslo = bcrypt.hashpw(haslo_bajty, sol).decode("utf-8")

    user = User(email=email, hashed_password=zahashowane_haslo)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def zaloguj_uzytkownika(email, haslo):
    user = session.query(User).filter(User.email == email).first()

    if not user:
        raise ValueError("Niepoprawny email lub hasło.")

    haslo_bajty = haslo.encode("utf-8")
    zahashowane_haslo_bajty = user.hashed_password.encode("utf-8")

    if not bcrypt.checkpw(haslo_bajty, zahashowane_haslo_bajty):
        raise ValueError("Niepoprawny email lub hasło.")

    stworz_token()
    return user

