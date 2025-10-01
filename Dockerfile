## SOLO PARA REFERENCIA

# Usar Python 3.12.5 slim
FROM python:3.12.5-slim

# Establecer directorio de trabajo
WORKDIR /src

# Copiar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY ./src ./src

# Inicializar la base de datos SQLite
RUN python -m src.seed_db

# Exponer puerto de FastAPI
EXPOSE 8000

# Comando por defecto para iniciar FastAPI
CMD ["python", "-m", "src.main"]
