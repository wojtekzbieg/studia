from sqlalchemy.orm import declarative_base
import pandas as pd
from connection import SessionLocal, engine
from models import Movie, Tag, Rating, Link, User


Base = declarative_base()


#       WCZYTYWANIE PLIKOW DO BAZY - DATAFRAME
def wczytaj_plik(plik, klasa, session):
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


if __name__ == "__main__":

    session = SessionLocal()

    try:
        #      UTWORZENIE TABEL W BAZIE JESLI ICH NIE MA
        # Base.metadata.create_all(engine)
        # print("Utworzono tabele.")

        #       WCZYTYWANIE PLIKOW DO BAZY
        # wczytaj_plik("data/movies.csv", Movie, session)
        # wczytaj_plik("data/tags.csv", Tag, session)
        # wczytaj_plik("data/ratings.csv", Rating, session)
        # wczytaj_plik("data/links.csv", Link, session)

        #       USUNIECIE ZAWARTOSCI TABELI
        # session.query(Movie).delete()
        # print("Usunięto zawartość tabeli")


        #      COMMIT ZMIAN
        # session.commit()
        # print("Zatwierdzono zmiany w bazie danych.")

        pass

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        # W razie błędu wycofujemy zmiany
        session.rollback()

    finally:
        session.close()

