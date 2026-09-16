# Seguridad

## 1. Descripción

La seguridad se divide entre la protección de la aplicación web y la seguridad de la infraestructura simulada.

## 2. Componentes

```text
seguridad/
├── access_control.py
├── audit.py
├── firewall.py
├── ids.py
├── policies.py
└── security_manager.py
```

## 3. Control de acceso

`access_control.py` contiene la lógica relacionada con permisos y acceso.

La aplicación utiliza roles, principalmente:

- `ADMIN`
- `VIEWER`

Las rutas administrativas requieren permisos de administrador.

## 4. Firewall

`firewall.py` implementa un firewall lógico para la infraestructura simulada.

Las reglas pueden definir:

- zona de origen;
- zona de destino;
- protocolo;
- puerto;
- acción.

Las acciones principales son `ALLOW` y `DENY`.

## 5. Zonas

`policies.py` define las zonas:

```text
IT
DMZ
OT
CONTROL
SAFETY
```

La separación permite representar una arquitectura segmentada.

## 6. IDS

`ids.py` implementa un detector basado en patrones de conexiones.

El contador de conexiones utiliza umbrales para producir estados `WARNING` y `CRITICAL`.

## 7. SecurityManager

`security_manager.py` coordina los componentes de seguridad.

## 8. Auditoría

`audit.py` registra acciones y eventos relevantes para permitir trazabilidad.

## 9. Seguridad de Flask

La aplicación incorpora:

- CSRF;
- rate limiting;
- cookies HttpOnly;
- SameSite;
- cabeceras de seguridad;
- Content Security Policy;
- X-Frame-Options;
- X-Content-Type-Options;
- Referrer-Policy;
- Permissions-Policy.

La clave secreta de Flask se obtiene mediante la variable de entorno `FLASK_SECRET_KEY`.

## 10. Limitaciones

La seguridad implementada tiene finalidad educativa y de laboratorio. Un entorno de producción requeriría, entre otras cosas, almacenamiento compartido para rate limiting, HTTPS correctamente configurado, gestión de secretos y una arquitectura de despliegue endurecida.
