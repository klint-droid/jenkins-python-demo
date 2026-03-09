from app import app

def test_add():
    client = app.test_client()
    response = client.get("/add?a=2&b=6")
    assert response.data == b"8"