from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_link = "sqlite:///./baza_danych.db"
engine = create_engine(db_link, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def stworz_sesje():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


