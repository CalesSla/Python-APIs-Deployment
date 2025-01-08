from app import schemas
from .database import client, session

def test_root(client):
    res = client.get("/")
    assert res.json().get("message") == "Hello World"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", 
                      json={"email": "hello1234@gmail.com",
                            "password": "password123"}
                      )
    
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello1234@gmail.com"
    assert res.status_code == 201
    

def test_login_user(client):
    
    res = client.post("/login", 
                      data={"username": "hello1234@gmail.com",
                            "password": "password123"}
                      )
    print(res.json())
    assert res.status_code == 200
