import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator
from src.routers import auth, products
from .db import Base, engine

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TechNova Inventory System")

# Activar métricas en /metrics
Instrumentator().instrument(app).expose(app)

# Rutas
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(products.router, prefix="/products", tags=["Products"])

# Archivos estáticos y templates
app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")
app.templates = templates


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
