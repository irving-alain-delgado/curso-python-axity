from fastapi.testclient import TestClient
from orders_service.api.main import app

client = TestClient(app)


def test_create_order_api():
    response = client.post(
        "/orders",
        json={
            "user_id": "user1",
            "product": "Laptop",
            "quantity": 1,
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "CREATED"
    assert "id" in data