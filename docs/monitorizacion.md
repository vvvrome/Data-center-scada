# Monitorización y alertas

## 1. Descripción

El paquete `monitorizar` contiene las métricas, logs y alertas del datacenter.

```text
monitorizar/
├── metrics.py
├── loggers.py
└── alerts.py
```

## 2. Métricas

`metrics.py` contiene la lógica relacionada con la obtención y tratamiento de métricas.

Las métricas permiten observar el comportamiento de servidores y dispositivos.

Entre las magnitudes utilizadas se encuentran:

- CPU;
- RAM;
- temperatura;
- consumo;
- tráfico;
- estado.

## 3. AlertManager

`alerts.py` contiene `AlertManager`, utilizado por el motor de simulación.

Durante cada ciclo se comprueba el estado de los elementos y, si se cumplen las condiciones definidas, se generan alertas.

## 4. Persistencia de una condición

El sistema contempla tiempos de persistencia para evitar que una fluctuación instantánea provoque necesariamente una alerta inmediata.

El comportamiento se puede representar como:

```text
Condición anómala
       |
       v
Comienza temporizador
       |
       +---- desaparece --> no se confirma
       |
       +---- persiste ----> alerta
```

## 5. Logs

`loggers.py` centraliza funciones relacionadas con el registro de información.

Los logs son importantes para estudiar posteriormente el comportamiento del laboratorio.

## 6. Evolución prevista

Una evolución natural es enviar estos eventos a Wazuh para centralizar logs, correlacionar eventos y construir reglas de detección.
