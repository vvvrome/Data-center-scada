# Infraestructura del datacenter

## 1. Descripción

El paquete `infraestructura` modela los componentes principales del centro de datos.

```text
DataCenter
   |
   +-- Rack
        +-- Server
        +-- Switch
        +-- Router
        +-- Storage
        +-- UPS
```

## 2. DataCenter

`infraestructura/datacenter.py` representa el centro de datos y mantiene la colección de racks.

La configuración puede cargarse desde `config/datacenter.yaml`.

## 3. Rack

`rack.py` representa un rack físico y organiza los dispositivos instalados.

Los racks permiten agrupar servidores y dispositivos de red para su posterior actualización y monitorización.

## 4. Server

`server.py` representa servidores del laboratorio.

El modelo contempla métricas de utilización y estado que pueden ser modificadas por el motor de simulación.

Entre las variables utilizadas se encuentran CPU, memoria, temperatura, consumo y tráfico.

## 5. Switch

`switch.py` representa switches de red.

El sistema puede monitorizar su estado y la utilización de sus puertos.

## 6. Router

`router.py` representa routers y permite incluirlos dentro del modelo de conectividad.

## 7. Storage

`storage.py` representa recursos de almacenamiento.

## 8. UPS

`ups.py` representa sistemas de alimentación ininterrumpida.

## 9. Estados

Los elementos monitorizados utilizan estados para representar su situación operacional, incluyendo condiciones normales y situaciones de advertencia o criticidad.

## 10. Relación con ASIR

Este módulo aplica conceptos de sistemas, hardware, redes, capacidad, disponibilidad y organización de infraestructura.
