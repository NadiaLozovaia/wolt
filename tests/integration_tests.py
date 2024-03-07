from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
URL = "/delivery_fee"


def test_read_main():
    response = client.post(
        URL,
        json={
            "cart_value": 790,
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-15T13:00:00Z",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 710}


def test_no_json():
    response = client.post(
        URL,
    )
    assert response.status_code == 422

def test_wrong_json():
    response = client.post(
        URL,
        json={
            "cart_value": "aaa",
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-15T13:00:00Z",
        },
    )
    assert response.status_code == 422
def test_wrong_json():
    response = client.post(
        URL,
        json={
            "cart_value": -1,
            "delivery_distance": 2235,
            "number_of_items": 4,
            "time": "2024-01-15T13:00:00Z",
        },
    )
    assert response.status_code == 422


