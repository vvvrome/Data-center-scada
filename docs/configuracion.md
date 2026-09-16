# Configuración

## 1. Configuración del datacenter

La configuración principal del datacenter se encuentra en:

```text
config/datacenter.yaml
```

## 2. Cargador

`config/loader.py` se encarga de cargar la configuración y convertirla en estructuras utilizables por el sistema.

El flujo conceptual es:

```text
datacenter.yaml
      |
      v
loader.py
      |
      v
DataCenter
      |
      v
Infraestructura
```

## 3. Ventajas

Separar configuración y código permite:

- cambiar la infraestructura sin modificar las clases;
- crear diferentes escenarios;
- mantener parámetros fuera de la lógica;
- facilitar experimentación.

## 4. Configuración de fallos

La configuración también puede proporcionar parámetros relacionados con los fallos utilizados por la planta.

El `SimulationEngine` pasa la configuración de fallos al constructor de `NuclearPlant`.

## 5. Variables sensibles

La clave secreta de Flask no se almacena en YAML ni en el código.

Debe proporcionarse mediante:

```text
FLASK_SECRET_KEY
```

## 6. Recomendación

Los secretos, credenciales y bases de datos locales deben excluirse del repositorio cuando contengan información sensible.
