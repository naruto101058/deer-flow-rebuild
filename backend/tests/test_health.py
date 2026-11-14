from fastapi.testclient import TestClient
from app.gateway.app import app

def test_health():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy", "service": "deerflow-rebuild"}
