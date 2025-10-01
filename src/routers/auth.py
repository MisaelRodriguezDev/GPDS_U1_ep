from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from src.db import get_db
from src.models import User
from src.utils import hash_pwd, check_password

router = APIRouter()


@router.get("/register")
def register_form(request: Request):
    return request.app.templates.TemplateResponse(
        "register.html", {"request": request}
    )


@router.post("/register")
def register(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    hashed_password = hash_pwd(password)
    user = User(username=username, password=hashed_password)
    db.add(user)
    db.commit()
    return RedirectResponse("/auth/login", status_code=302)


@router.get("/login")
def login_form(request: Request):
    return request.app.templates.TemplateResponse(
        "login.html", {"request": request}
    )


@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.username == username
    ).first()
    if user and check_password(password, user.password):
        return RedirectResponse("/", status_code=302)
    return {"error": "Credenciales inválidas"}
