from fastapi.testclient import TestClient
from fastapi_lab.main import app

client = TestClient(app)


def test_create_order(test_client):
    response = test_client.post("/orders/", json={"amount": 100})
    assert response.status_code == 401  # ahora requiere token