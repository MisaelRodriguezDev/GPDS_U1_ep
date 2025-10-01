from fastapi.testclient import TestClient
from src.main import app
from src.db import get_db
from src.models import User
from sqlalchemy.orm import Session
from src.utils import hash_pwd

client = TestClient(app)

def test_login_valid():
    username = "admin"
    password = "admin123"

    # Asegurarse de que el usuario exista
    db: Session = next(get_db())
    user = db.query(User).filter(User.username == username).first()
    if not user:
        user = User(username=username, password=hash_pwd(password))
        db.add(user)
        db.commit()
    db.close()

    # Login con credenciales válidas
    response = client.post("/auth/login", data={"username": username, "password": password})
    assert response.status_code == 200 
