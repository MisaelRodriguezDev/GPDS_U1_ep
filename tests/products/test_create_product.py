from fastapi.testclient import TestClient
from src.main import app
from src.db import get_db
from src.models import Product
from sqlalchemy.orm import Session

client = TestClient(app)

def test_create_product():
    db: Session = next(get_db())

    # Limpiar producto de prueba si existe
    product_name = "Test Product"
    existing = db.query(Product).filter(Product.name == product_name).first()
    if existing:
        db.delete(existing)
        db.commit()

    # Crear producto mediante formulario
    product_data = {
        "name": product_name,
        "description": "Producto de prueba",
        "price": 99.99,
        "stock": 10
    }
    response = client.post("/products/create", data=product_data)
    assert response.status_code == 200

    # Verificar existencia en DB
    product = db.query(Product).filter(Product.name == product_name).first()
    assert product is not None
    db.close()
