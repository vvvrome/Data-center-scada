# Limitaciones

## 1. Naturaleza del proyecto

DataCenter Lab es un laboratorio software de simulación y experimentación.

No pretende sustituir herramientas profesionales de monitorización, sistemas ICS/SCADA, simuladores nucleares ni equipos de comunicaciones cuánticas.

## 2. Modelos físicos

Los modelos térmicos y de proceso son simplificaciones.

Los valores utilizados no deben interpretarse como parámetros reales de una instalación nuclear.

## 3. Planta nuclear

La planta tiene finalidad educativa y no representa un sistema de control nuclear real.

No debe utilizarse para diseñar, operar o evaluar una instalación física.

## 4. Red

Routers, switches, firewall e IDS son modelos software. No representan por sí mismos el comportamiento completo de equipos de red o dispositivos industriales reales.

## 5. QKD

La implementación QKD es una simulación del protocolo y no utiliza hardware cuántico real.

## 6. Base de datos

SQLite es adecuada para un laboratorio local. Un despliegue distribuido requeriría una arquitectura de persistencia diferente.

## 7. Rate limiting

La configuración actual utiliza `memory://`. Este almacenamiento no es compartido entre múltiples instancias de aplicación.

## 8. Seguridad web

La CSP actual mantiene `unsafe-inline` para compatibilidad con el frontend existente. Una evolución futura podría eliminar esta dependencia mediante scripts externos y nonces o hashes.

## 9. Testing

La cobertura automatizada es parcial y se concentra actualmente en QKD.

## 10. Escalabilidad

El proyecto está orientado principalmente a experimentación local. Un despliegue de producción requeriría una arquitectura distribuida, almacenamiento compartido, observabilidad y gestión de secretos más avanzada.
