from .db import SessionLocal, Base, engine
from .models import User, Product
from .utils import hash_pwd

# Crear tablas (si no existen)
Base.metadata.create_all(bind=engine)

# Crear contexto de sesión
db = SessionLocal()


# --- Crear usuario de prueba ---
test_user = db.query(User).filter(
    User.username == "admin"
).first()
if not test_user:
    user = User(
        username="admin",
        password=hash_pwd("admin123")
    )
    db.add(user)
    print("Usuario 'admin' creado con contraseña 'admin123'")

# --- Crear productos de ejemplo ---
sample_products = [
    {
        "name": "Laptop",
        "description": "Laptop 16GB RAM",
        "price": 1200.00,
        "stock": 10
    },
    {
        "name": "Mouse",
        "description": "Mouse inalámbrico",
        "price": 25.50,
        "stock": 50
    },
    {
        "name": "Teclado",
        "description": "Teclado mecánico",
        "price": 80.00,
        "stock": 30
    },
    {
        "name": "Monitor",
        "description": "Monitor 24 pulgadas",
        "price": 200.00,
        "stock": 15
    }
]

for p in sample_products:
    exists = db.query(Product).filter(
        Product.name == p["name"]
    ).first()
    if not exists:
        product = Product(**p)
        db.add(product)
        print(f"Producto '{p['name']}' agregado")

# Confirmar cambios
db.commit()
db.close()
print("Base de datos inicializada correctamente")
