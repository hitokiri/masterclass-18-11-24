# Proyecto de Masterclass de Docker y Kubernetes


Este proyecto contiene ejemplos y materiales presentados en la masterclass de Docker y Kubernetes. A continuación se describe la estructura de carpetas y archivos del proyecto.

## Estructura del Proyecto

### Documentos

- **Cikume_Software_masterclass_docker_y_kubernetes.pptx**: Presentación de la masterclass de Docker y Kubernetes.
- **Kubernetes masterclass.pptx**: Otra presentación relacionada con Kubernetes.

### Ejemplos_presentados

#### docker_file_multy_stage

- **.dockerignore**: Archivo para excluir archivos y directorios en el contexto de construcción de Docker.
- **compose.yaml**: Archivo de configuración de Docker Compose para el servicio frontend.
- **Dockerfile.dev**: Dockerfile para el entorno de desarrollo.
- **log_build**: Registro de la construcción de la imagen Docker.
- **package.json**: Archivo de configuración de npm para el proyecto frontend.
- **public/**: Carpeta que contiene archivos públicos, como `index.html`.
- **src/**: Carpeta que contiene el código fuente del proyecto frontend.

#### ejemplo_completo

- **.env**: Archivo de variables de entorno.
- **.mypy_cache/**: Carpeta de caché de mypy.
- **compose.yaml**: Archivo de configuración de Docker Compose para el proyecto completo.
- **frontend/**: Carpeta que contiene el código fuente del frontend.
- **migraciones/**: Carpeta para archivos de migración de base de datos.
- **postgres-data/**: Carpeta para datos de PostgreSQL.

#### kubernetes_examples

- **app.yaml**: Archivo de configuración de Kubernetes para la aplicación.
- **Docker_kubernetes_master_class/**: Carpeta con ejemplos de Docker y Kubernetes.
- **kustomizer/**: Carpeta con configuraciones de Kustomize.

## Cómo Usar

### Docker

Para construir y ejecutar el servicio frontend en `docker_file_multy_stage`, usa los siguientes comandos:

```sh
cd Ejemplos_presentados/docker_file_multy_stage
docker-compose up --build



# Contenido del Proyecto

- **Cikume_Software_masterclass_docker_y_kubernetes.pptx**: Presentación de la masterclass de Docker y Kubernetes.
- **Kubernetes masterclass.pptx**: Otra presentación relacionada con Kubernetes.

### Ejemplos_presentados

#### docker_file_multy_stage

- **.dockerignore**: Archivo para excluir archivos y directorios en el contexto de construcción de Docker.
- **compose.yaml**: Archivo de configuración de Docker Compose para el servicio frontend.
- **Dockerfile.dev**: Dockerfile para el entorno de desarrollo.
- **log_build**: Registro de la construcción de la imagen Docker.
- **package.json**: Archivo de configuración de npm para el proyecto frontend.
- **public/**: Carpeta que contiene archivos públicos, como `index.html`.
- **src/**: Carpeta que contiene el código fuente del proyecto frontend.

#### ejemplo_completo

- **.env**: Archivo de variables de entorno.
- **.mypy_cache/**: Carpeta de caché de mypy.
- **compose.yaml**: Archivo de configuración de Docker Compose para el proyecto completo.
- **frontend/**: Carpeta que contiene el código fuente del frontend.
- **migraciones/**: Carpeta para archivos de migración de base de datos.
- **postgres-data/**: Carpeta para datos de PostgreSQL.

#### kubernetes_examples

- **app.yaml**: Archivo de configuración de Kubernetes para la aplicación.
- **Docker_kubernetes_master_class/**: Carpeta con ejemplos de Docker y Kubernetes.
- **kustomizer/**: Carpeta con configuraciones de Kustomize.

## Cómo Usar

### Docker

Para construir y ejecutar el servicio frontend en `docker_file_multy_stage`, usa los siguientes comandos:

```sh
cd Ejemplos_presentados/docker_file_multy_stage
docker-compose up --build