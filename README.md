# FastAPI **Property API**
This a **CRU API** designed to handle REST petitions to **create, read and update** properties in a mongo database. It can save images in a static folder and asociate them to properties. It can also create owners and asociate the properties to them. The price of a property with a given ID can be updated. **Testing** has been implemented for the method in the routers for both the properties and the owners.

## Steps to try the **Property API**

1. **Clone the repository**
2. **Create a virtual environment**
    % python -m venv env
3. **Install the requirements**
    % pip install -r requirements.txt
4. **Run the tests**
    % pytest
5. **Run the API**
    % python main.py
6. **Enjoy**

You can access the API in your browser using the url:
    http://127.0.0.1:8000/
The **documentation** can be visited in the swagger using the url:
    http://127.0.0.1:8000/docs
There you can test all the features.
