# API y aplicación web

## 1. Descripción

La aplicación web está implementada con Flask y se encuentra principalmente en `API/app.py`.

## 2. Inicialización

La función `create_app()` recibe componentes del laboratorio y crea la aplicación Flask.

Entre los componentes utilizados se encuentran:

- datacenter;
- alert manager;
- security manager;
- planta;
- creación de usuarios.

## 3. Seguridad de la aplicación

Durante la inicialización se configuran:

- `SECRET_KEY`;
- sesiones;
- CSRF;
- rate limiting;
- cabeceras de seguridad.

La clave secreta se obtiene desde `FLASK_SECRET_KEY`.

## 4. Autenticación

La aplicación incluye rutas para:

- `/login`
- `/logout`
- `/register`

El login crea una sesión asociada al usuario y su rol.

## 5. Control de acceso

Existe un decorador `login_required()` que comprueba:

1. si existe una sesión;
2. si el usuario sigue existiendo;
3. si posee el rol requerido cuando la ruta lo exige.

## 6. Administración

La aplicación incluye funcionalidades administrativas relacionadas con:

- usuarios;
- registros de auditoría.

El acceso está restringido al rol correspondiente.

## 7. Graph Lab

La aplicación registra el blueprint de Graph Lab para integrar sus rutas dentro de Flask.

## 8. Auditoría

Las acciones relevantes pueden registrarse mediante `audit()` y el módulo de base de datos correspondiente.

## 9. Cabeceras

Se añaden cabeceras como:

```text
X-Content-Type-Options
X-Frame-Options
Referrer-Policy
Permissions-Policy
Content-Security-Policy
```

## 10. Limitación del rate limiting

Actualmente se utiliza `memory://`, apropiado para desarrollo y laboratorio. En una aplicación distribuida se recomienda utilizar un almacenamiento compartido.
