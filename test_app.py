import pytest
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Hello from Flask in Docker!"

def test_echo():
    client = app.test_client()
    response = client.post("/echo", json={"message": "hello"})

    assert response.status_code == 200
    assert response.get_json() == {"you_sent": {"message": "hello"}}

