# SOLO DE REFERENCIA

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
  required_version = ">= 1.3.0"
}

provider "docker" {}

# Construir la imagen desde tu Dockerfile
resource "docker_image" "fastapi_app" {
  name = "gpds-ep:latest"
  build {
    context    = "../"
    dockerfile = "../Dockerfile"
  }
}

# Crear contenedor a partir de la imagen
resource "docker_container" "fastapi_container" {
  name  = "fastapi_app"
  image = docker_image.fastapi_app.image_id

  ports {
    internal = 8000
    external = 8000
  }

  # Si se quiere montar el archivo de base de datos SQLite en volumen
  # para que no se borre al reiniciar el contenedor:
  mounts {
    target = "/src/src/database.db"
    source = "${path.module}/../src/database.db"
    type   = "bind"
  }
}

# Prometheus
resource "docker_container" "prometheus" {
  name  = "prometheus"
  image = "prom/prometheus:latest"

  ports {
    internal = 9090
    external = 9090
  }

  volumes {
    host_path      = "${path.module}/prometheus.yml"
    container_path = "/etc/prometheus/prometheus.yml"
  }
}

# Grafana
resource "docker_container" "grafana" {
  name  = "grafana"
  image = "grafana/grafana:latest"

  ports {
    internal = 3000
    external = 3000
  }

  # Persistir datos de Grafana
  volumes {
    host_path      = "${path.module}/grafana-data"
    container_path = "/var/lib/grafana"
  }
}
