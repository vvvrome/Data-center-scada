# Arquitectura del sistema

## 1. Descripción

DataCenter Lab es una aplicación modular que integra simulación de infraestructura informática, monitorización, seguridad, una planta crítica simplificada y herramientas de análisis matemático.

La versión integrada se organiza alrededor de una aplicación Flask y de un motor de simulación que coordina los diferentes componentes.

## 2. Arquitectura general

```text
                         Usuario
                            |
                            v
                     Aplicación Flask
                            |
          +-----------------+------------------+
          |                 |                  |
          v                 v                  v
     DataCenter         Seguridad          Graph Lab
          |                 |                  |
          v                 v                  v
     Simulación        Firewall / IDS     Análisis gráfico
          |
          v
    Monitorización
          |
          v
        Alertas

                            |
                            v
                    Planta crítica
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
          Reactor       Sensores       Actuadores
             |              |
             +--------------+
                    |
                    v
              Seguridad OT
                    |
                    v
                   QKD
```

## 3. Capas

### Presentación

La interfaz utiliza Flask, Jinja2, HTML, CSS y JavaScript.

### Aplicación

Flask gestiona autenticación, sesiones, rutas, administración y acceso a los datos del laboratorio.

### Simulación

`SimulationEngine` coordina las actualizaciones periódicas del datacenter y de la planta.

### Dominio

Los paquetes `infraestructura`, `planta`, `seguridad`, `monitorizar` y `graph_lab` contienen la lógica específica de cada área.

### Persistencia

SQLite almacena usuarios y eventos de auditoría.

## 4. Flujo principal

```text
main.py
   |
   +--> configuración YAML
   |
   +--> DataCenter
   |
   +--> SimulationEngine
   |
   +--> Flask
   |
   +--> actualización periódica
```

## 5. Ventajas de la arquitectura

- Separación de responsabilidades.
- Posibilidad de ampliar módulos individualmente.
- Configuración de infraestructura independiente del código.
- Separación entre simulación y presentación.
- Posibilidad de añadir herramientas externas de monitorización.

## 6. Alcance

La arquitectura representa un laboratorio educativo. Los elementos industriales, físicos y cuánticos son modelos software simplificados.
