from sqlalchemy.orm import declarative_base
import pandas as pd
from connection import session, engine
from models import Movie, Tag, Rating, Link


Base = declarative_base()


#       DATAFRAME
def wczytaj_plik(plik, klasa):
    df = pd.read_csv(plik)
    tuples = df.itertuples(index=False)
    for i in tuples:
        print(i)
        obiekt = klasa(**i._asdict())
        session.add(obiekt)

#       LISTA PYTHONOWA
# def wczytaj_plik(plik, klasa):
#     with open(plik, mode = "r", encoding="utf-8") as file:
#         plikCSV = csv.DictReader(file)
#         for i in plikCSV:
#             obiekt = klasa(**i)
#             # print(obiekt.title)
#             session.add(obiekt)


#       WCZYTYWANIE PLIKOW DO BAZY
wczytaj_plik("data/movies.csv", Movie)
wczytaj_plik("data/tags.csv", Tag)
wczytaj_plik("data/ratings.csv", Rating)
wczytaj_plik("data/links.csv", Link)

#      USUNIECIE ZAWARTOSCI TABELI
# session.query(Movie).delete()

#      COMMIT ZMIAN
# session.commit()

#      UTWORZENIE TABEL W BAZIE JESLI ICH NIE MA
# Base.metadata.create_all(engine)

