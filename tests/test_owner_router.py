# tests/test_property_router.py
from fastapi.testclient import TestClient
from main import app
from app.adapters.databases.owner_database import MongoDBOwnerRepository
from app.core.models.owner import Owner
from mongomock import MongoClient

def setup_module():
    # Replace the real MongoDB connection with mongomock during testing
    MongoDBOwnerRepository.client = MongoClient('mongodb://localhost:27017/test_database')

def teardown_module():
    # Clear the in-memory database after all tests are executed
    MongoDBOwnerRepository.client.drop_database('test_database')

client = TestClient(app)

# Setup: Create a test owner
id_owner = "0"
test_owner = Owner(IdOwner=id_owner, Name="John Doe", Address="039 Broad Av", Photo="http://photo_url1", Birthday="20-01-1990")

def test_create_owner():
    
    #Action: Send a test request to create a owner
    response = client.post("/api/owners/", json=test_owner.model_dump())

    # Assertion: Check if the owner was created successfully
    assert response.status_code == 200
    assert response.json() == test_owner.model_dump()

def test_get_owner_by_id():
    #Action: Send a test request to get a owner by id
    response = client.get("api/owners/"+id_owner)

    # Assertion: Check if the owner is in the response
    assert response.status_code == 200
    assert response.json() == test_owner.model_dump()