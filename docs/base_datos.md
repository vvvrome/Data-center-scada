# Base de datos

## 1. Descripción

El proyecto utiliza SQLite para almacenar información persistente relacionada principalmente con usuarios y auditoría.

## 2. Estructura

```text
database/
├── users.py
├── audit.py
├── create_admin.py
└── users.db
```

## 3. Usuarios

`users.py` contiene las funciones relacionadas con la creación, autenticación y consulta de usuarios.

La aplicación utiliza roles para controlar el acceso.

## 4. Roles

Los principales roles utilizados son:

- `ADMIN`
- `VIEWER`

Los usuarios registrados desde la aplicación se crean con el rol `VIEWER`.

## 5. Auditoría

`audit.py` permite registrar acciones relevantes.

Los eventos pueden incluir:

- login correcto;
- login fallido;
- logout;
- registro;
- acceso administrativo;
- bloqueos CSRF;
- eventos de seguridad.

La información de auditoría incluye datos como usuario, acción, resultado, dirección IP, User-Agent, detalles y timestamp.

## 6. Administrador inicial

`create_admin.py` permite crear el usuario administrador inicial.

Las credenciales utilizadas durante el desarrollo no deben almacenarse en el repositorio.

## 7. Base de datos local

El archivo `users.db` es una base de datos local del laboratorio.

Se recomienda excluir bases de datos de desarrollo del repositorio mediante `.gitignore` cuando contengan datos reales o temporales.
