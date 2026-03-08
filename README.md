# Sistema de Inventario

Aplicación de escritorio desarrollada en **Python** para la gestión de productos utilizando una base de datos **MySQL** y una interfaz gráfica construida con **Tkinter**.

Este proyecto permite realizar operaciones básicas de inventario como agregar, visualizar, actualizar y eliminar productos.

---

## Funcionalidades

* Agregar productos al inventario
* Visualizar lista de productos
* Actualizar información de productos
* Eliminar productos del inventario

---

## Tecnologías utilizadas

* Python 3
* Tkinter
* MySQL
* mysql-connector-python
* python-dotenv

---

## Instalación

1. Clonar el repositorio

```
git clone https://github.com/mailyndev/sistema_inventario.git
cd sistema_inventario
```

2. Crear un entorno virtual (opcional pero recomendado)

```
python -m venv venv
```

Activar entorno virtual

Windows:

```
venv\Scripts\activate
```

3. Instalar dependencias

```
pip install -r requirements.txt
```

---

## Configuración

1. Crear un archivo `.env` basado en `.env.example`.

2. Completar los datos de conexión a la base de datos.

Ejemplo:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=inventario_db
```

---

## Base de datos

El archivo `inventario.sql` contiene el script necesario para crear la base de datos y la tabla de productos.

Ejecuta el script en tu servidor MySQL antes de iniciar la aplicación.

---

## Ejecutar la aplicación

```
python app.py
```

---

## Autor

Desarrollado por **mailyndev** como proyecto de práctica para aprender desarrollo con Python y bases de datos.
