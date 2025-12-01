# Proyecto Jen

## Getting Started

Este repositorio está dividido en dos partes: **frontend** y
**backend**.\
El frontend está desarrollado en **React** y el backend en **Django**.

A continuación se explica cómo iniciar cada entorno por separado.

## Requisitos

Asegúrate de tener instalado:

-   npm y npx (gestores de paquetes de JavaScript)
-   Python 3.11 y Django

Para instalar Django puedes usar `pip`:

``` bash
pip install django
```

## Frontend

1.  Entra en la carpeta del frontend:

``` bash
cd frontend
```

2.  Instala las dependencias:

``` bash
npm install
```

3.  Inicia el servidor de desarrollo:

``` bash
npm run start
```

El proyecto se montará en un puerto local, permitiendo ver los cambios
en tiempo real.

## Backend (Django)

1.  Entra en la carpeta del backend:

``` bash
cd backend
```

2.  Verifica que Django está instalado:

``` bash
python -m django --version
```

3.  Ejecuta las migraciones:

``` bash
python manage.py migrate
```

4.  Inicia el servidor de desarrollo:

``` bash
python manage.py runserver
```

El backend quedará disponible en el servidor local.
