from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from src.db import get_db
from src.models import Product

router = APIRouter()


@router.get("/")
def list_products(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return request.app.templates.TemplateResponse(
        "products.html", {"request": request, "products": products}
    )


@router.post("/create")
def create_product(
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...),
    db: Session = Depends(get_db)
):
    product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock
    )
    db.add(product)
    db.commit()
    return RedirectResponse("/products", status_code=302)
