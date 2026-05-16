from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200


def test_get_restaurants():

    response = client.get("/api/restaurants")

    assert response.status_code == 200