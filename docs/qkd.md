# Simulación QKD / BB84

## 1. Descripción

La planta incorpora una simulación educativa de distribución cuántica de claves basada en el protocolo BB84.

## 2. Componentes

```text
Alice
  |
  v
Quantum Channel
  |
  v
Bob
  |
  v
QKD Manager
```

El módulo también incluye un detector de intrusiones y un mecanismo para gestionar sesiones.

## 3. Proceso simplificado

```text
Generación de bits
        |
        v
Selección de bases
        |
        v
Envío por canal
        |
        v
Medición
        |
        v
Comparación de bases
        |
        v
Clave compartida
```

## 4. QBER

QBER representa la tasa de error de bits cuánticos.

Dentro de la simulación se utiliza como indicador del estado de una sesión.

```text
QBER bajo
   |
   v
Estado normal

QBER elevado
   |
   v
Posible interferencia
   |
   v
Sesión comprometida
```

## 5. QKDManager

`qkd_manager.py` gestiona información sobre sesiones, incluyendo:

- sesiones;
- sesiones exitosas;
- sesiones comprometidas;
- QBER;
- historial;
- longitud de clave;
- estado del canal.

## 6. QuantumChannel

`quantum_channel.py` representa el canal utilizado por la simulación.

## 7. IntrusionDetector

`intrusion_detector.py` permite detectar condiciones relacionadas con interferencias o anomalías de la simulación.

## 8. Limitaciones

La implementación es una simulación software. No representa hardware cuántico ni las propiedades físicas completas de un sistema QKD real.
