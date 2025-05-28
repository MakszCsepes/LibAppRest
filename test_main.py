from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

    assert response.json() == {"message": "Hello. Today is 2th day of the week!"}

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    
    # NOTE: order matters
    expected_response = {"books": [{"name": "book1", "category": "cat1", "date_published": "1990"},
                                   {"name": "book2", "category": "cat2", "date_published": "2002"}]}

    assert response.json() == expected_response