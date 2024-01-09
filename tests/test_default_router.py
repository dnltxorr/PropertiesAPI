# tests/test_defaul_router.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    
    #Action: Send a test request to the default router
    response = client.get("/")

    # Assertion: Check if the status of the home response
    assert response.status_code == 200
