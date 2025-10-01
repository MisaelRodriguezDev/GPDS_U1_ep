from fastapi.testclient import TestClient
from src.main import app
from src.db import get_db
from src.models import User
from sqlalchemy.orm import Session

client = TestClient(app)

def test_register_user():
    username = "testuser"
    password = "Test1234!"

    # Eliminar usuario si ya existe
    db: Session = next(get_db())
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        db.delete(existing_user)
        db.commit()
    db.close()

    # Registrar usuario mediante formulario
    response = client.post("/auth/register", data={"username": username, "password": password})
    assert response.status_code == 200

    # Verificar en DB
    db: Session = next(get_db())
    user = db.query(User).filter(User.username == username).first()
    assert user is not None
    db.close()
