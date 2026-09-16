# Simulación de planta crítica

## 1. Descripción

El paquete `planta` representa una planta nuclear simplificada con finalidad educativa.

No pretende reproducir una instalación nuclear real ni proporcionar parámetros de operación o control reales.

## 2. Arquitectura

```text
NuclearPlant
|
+-- Reactor
+-- Sensores
+-- Actuadores
+-- Controlador
+-- FaultManager
+-- SafetyController
+-- AlertManager
|
+-- Security
    +-- SecurityController
    +-- IntrusionDetector
    +-- QKDManager
    +-- QuantumChannel
    +-- QKD
```

## 3. Reactor

`reactor.py` contiene el modelo simplificado del reactor.

Se utilizan variables como:

- temperatura;
- presión;
- caudal;
- potencia;
- nivel de agua;
- radiación.

## 4. Proceso

`proceso.py` contiene `NuclearPlant` y coordina los diferentes componentes de la planta.

## 5. Sensores

`sensores.py` permite representar las mediciones del proceso.

## 6. Actuadores

`actuadores.py` representa elementos capaces de modificar variables del modelo.

## 7. Controlador

`controlador.py` contiene la lógica de control de la planta.

## 8. FaultManager

`fault_manager.py` permite gestionar fallos simulados.

## 9. SafetyController

`safety_controller.py` representa la lógica de seguridad del proceso.

## 10. Alertas

`alert_manager.py` gestiona alertas específicas de la planta.

## 11. Seguridad OT

La planta incorpora una capa de seguridad separada para representar la protección de comunicaciones y componentes relacionados con el proceso.

## 12. Alcance

El modelo es educativo. No debe interpretarse como un modelo de ingeniería, seguridad nuclear o control industrial real.
