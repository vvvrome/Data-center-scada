# Motor de simulación

## 1. Objetivo

El paquete `simulacion` convierte el modelo estático de infraestructura en un entorno dinámico.

## 2. SimulationEngine

El componente principal es `SimulationEngine`, definido en `simulacion/motor.py`.

Recibe el datacenter y la configuración y crea:

- generador de workload;
- gestor de alertas;
- gestor de seguridad;
- planta nuclear simulada.

## 3. Ciclo de actualización

En cada `update()`:

```text
1. Incrementar tick
2. Actualizar planta
3. Generar workload
4. Actualizar servidores
5. Comprobar servidores
6. Actualizar switches
7. Comprobar switches
8. Comprobar puertos
9. Actualizar routers
10. Comprobar routers
```

## 4. Workload

`workload.py` genera carga de trabajo sobre los servidores.

Esta carga modifica las métricas utilizadas posteriormente por la monitorización.

## 5. Power

`power.py` contiene la lógica relacionada con consumo energético.

## 6. Cooler

`cooler.py` representa la refrigeración y permite relacionar carga, generación de calor y temperatura dentro del modelo.

## 7. Network

`network.py` contiene lógica relacionada con el comportamiento de red simulado.

## 8. Failures

`failures.py` permite introducir condiciones de fallo para estudiar la respuesta del sistema.

## 9. Ejecución por ticks

El método `run()` permite ejecutar un número determinado de ciclos con un retardo configurable.

El objetivo es disponer de un reloj de simulación sencillo para experimentar con la evolución del sistema.
