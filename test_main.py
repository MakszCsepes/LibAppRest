from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

    message = response.json()["message"];

    assert "Hello. Today is " in message and \
           "th day of the week!" in message