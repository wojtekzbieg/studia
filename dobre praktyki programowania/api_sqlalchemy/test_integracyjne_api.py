from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

# def test_rejestracja():
#     testowyuser={
#         "email": "testowyemail5@gmail.com",
#         "haslo": "testowehaslo5"
#     }
#     response = client.post("/rejestracja", json=testowyuser)
#     assert response.status_code == 200

def test_logowanie():
    testowyuser = {
        "email": "testowyemail1@gmail.com",
        "haslo": "testowehaslo1"
    }
    response = client.post("/logowanie", json=testowyuser)
    assert response.status_code == 200
    assert "token" in response.json()

    testowyuser = {
        "email": "tgdslknfes@gmail.com",
        "haslo": "dfjgcvkhjblkno1"
    }
    response = client.post("/logowanie", json=testowyuser)
    assert response.status_code == 401


def test_user_details_z_tokenem():
    login_data = {
        "email": "jankowalski@gmail.com",
        "haslo": "qwerty123"
    }
    # Logowanie w celu uzyskania tokenu
    response_login = client.post("/logowanie", json=login_data)
    assert response_login.status_code == 200
    token = response_login.json()["token"]

    # Zapytanie z tokenem
    header = {"Authorization": f"Bearer {token}"}
    response_details = client.get("/user-details", headers=header)
    assert response_details.status_code == 200
    assert response_details.json()["sub"] == login_data["email"]


def test_user_details_bez_tokenu():
    response = client.get("/user-details")
    assert response.status_code == 401

def test_user_details_ze_zmodyfikowanym_tokenem():
    login_data = {
        "email": "jankowalski@gmail.com",
        "haslo": "qwerty123"
    }
    # Logowanie w celu uzyskania tokenu
    response_login = client.post("/logowanie", json=login_data)
    token = response_login.json()["token"]

    # Modyfikacja tokenu (np. zmiana jednego znaku)
    zmodyfikowany_token = token[:10] + "X" + token[10:]

    header = {"Authorization": f"Bearer {zmodyfikowany_token}"}
    response_details = client.get("/user-details", headers=header)
    assert response_details.status_code == 401