from fastapi.testclient import TestClient

from ..app import app

client = TestClient(app)


def test_read_event():
    response = client.get("/events/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": "",
        "name": "Foo",
        "description": "There goes my hero",
    }

def test_read_inexistent_item():
    response = client.get("/events/baz")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_create_item():
    response = client.post(
        "/events/",
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }


def test_create_item_bad_token():
    response = client.post(
        "/items/",
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_item():
    response = client.post(
        "/items/",
        json={
            "id": "foo",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Item already exists"}