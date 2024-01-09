# tests/test_property_router.py
import os
from fastapi.testclient import TestClient
from main import app
from app.adapters.databases.property_database import MongoDBPropertyRepository
from app.core.models.property import Property
from app.core.models.owner import Owner
from mongomock import MongoClient

def setup_module():
    # Replace the real MongoDB connection with mongomock during testing
    MongoDBPropertyRepository.client = MongoClient('mongodb://localhost:27017/test_database')

def teardown_module():
    # Clear the in-memory database after all tests are executed
    MongoDBPropertyRepository.client.drop_database('test_database')

client = TestClient(app)

# Setup: Create a test owner
id_owner = "0"
test_owner = Owner(IdOwner=id_owner, Name="John Doe", Address="039 Broad Av", Photo="http://photo_url1", Birthday="20-01-1990")

# Setup: Create a test property
id_property1="101"
test_property1 = Property(IdProperty=id_property1, Name="test1", Address="123 Main St", Price="10", CodeInternal="1607", Year="2022", Owner=id_owner)

# Setup: Create a test property in the database
id_property2="102"
test_property2 = Property(IdProperty=id_property2, Name="test2", Address="456 Oak Ave", Price="10", CodeInternal="1808", Year="2020", Owner=id_owner)

def test_create_property():
    
    #Action: Send a test request to create a owner
    client.post("/api/owners/", json=test_owner.model_dump())

    # Action: Send a test request to create the property
    response = client.post("/api/properties/", headers={"Content-Type": "application/json"},json=test_property1.model_dump())

    # Assertion: Check if the property was created successfully
    assert response.status_code == 200
    assert response.json() == test_property1.model_dump()

def test_get_properties():
    
    client.post("api/properties/",json=test_property2.model_dump())

    # Action: Send a test request to get properties
    response = client.get("/api/properties")

    # Assertion: Check if the property is in the response
    assert response.status_code == 200
    assert any(property["IdProperty"] == id_property2 for property in response.json())

def test_get_property_by_id():
    #Action: Send a test request to get a property by id
    response = client.get("api/properties/"+id_property2)

    # Assertion: Checking if the property is in the response
    assert response.status_code == 200
    assert response.json() == test_property2.model_dump()

def test_update_property_price():
    new_price = 5000.0
    #Action: Send a test request to update a property price
    response = client.put(f"api/properties/update-price/?id_property={id_property2}&new_price={new_price}")

    # Assertion: Check if the property has the new price
    assert response.status_code == 200
    assert response.json()["Price"] == new_price

def test_add_property_image():
    # Arrange: Setting up the properties and the image file.
    response = client.post("/api/properties/", headers={"Content-Type": "application/json"},json=test_property1.model_dump())

    file_path = "tests/test.png"
    
    with open(file_path, "rb") as file:
        file_content = file.read()

    files = {"file": ("test.png", file_content, "image/png")}

    # Action: Creating the Image
    response = client.post(
        "/api/properties/image-upload/",
        params={"id_property_image": "0", "id_property": f"{id_property1}", "enabled": True},
        files=files,
        headers={"accept": "multipart/form-data"},
    )

    files = os.listdir("static/images/")
    matching_files = [file for file in files if "test" in file]

    # Assertion: OK response and checking if the imagefile is in the images folder
    assert response.status_code == 200
    assert len(matching_files) > 0

    # Cleanup
    for file in matching_files:
        os.remove(f"static/images/{file}")

    # Assert that the file has been removed
    for file in matching_files:
        assert not os.path.exists(f"static/images/{file}")