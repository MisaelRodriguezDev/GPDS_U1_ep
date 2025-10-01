# TechNova Solutions - Gestión de Inventarios

## Descripción

Aplicación web para gestionar productos e inventarios con **FastAPI**, **SQLite**, **HTML/CSS/JS**. Incluye:
- Registro y login de usuarios.
- CRUD de productos.
- Generación de reportes.
- Integración CI/CD con pruebas automatizadas.

## Estructura
```text
GPDS_U1_ep/
├── src/
│   ├── routers/              # Enrutadores por módulo
│   ├── static/               # Archivos estáticos
│   ├── templates/            # Archivos HTML
│   ├── db.py                 # Configuración de la base de datos
│   ├── main.py               # Punto de entrada
│   ├── models.py             # Modelos de las tablas
│   ├── seed_db.py            # Script para crear la base de datos
|   └── utils.py              # Funciones utilitarias
├── docs/                     # Documentación técnica
├── tests/
│   ├── auth/                 # Pruebas de authenticación
│   ├── manual/               # Pruebas manuales
│   └── products/             # Pruebas de productos
├── requirements.txt          # Dependencias
└── README.md                 
```

## Instalación
*Nota: Los pasos que usan docker slo son de referencia

1. Clona el repositorio
```bash
$ git clone https://github.com/MisaelRodriguezDev/GPDS_U1_ep.git
```

2. Construye la imagen
```bash
$ docker build -t gpds-ep .
```

O crea el entorno virtual
```bash
$ python -m venv .venv
```

Instala las dependencias
```bash
$ pip install -r requirements.txt
```

3. Ejecuta el contenedor
```bash
$ docker run -d -p 8000:8000 --name pds-ep-container gpds-ep
```

o ejecuta con python
```bash
$ python -m src.main
```

## Autor
Misael Rodríguez
