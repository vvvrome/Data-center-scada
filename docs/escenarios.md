# Escenarios experimentales

## 1. Objetivo

Los escenarios permiten comprobar el comportamiento del laboratorio bajo diferentes condiciones.

Cada escenario debería registrar:

- condición inicial;
- acción realizada;
- variables observadas;
- estado final;
- alertas;
- logs generados.

## 2. Funcionamiento normal

### Condición

La infraestructura trabaja dentro de los valores esperados.

### Flujo

```text
Carga normal
    |
    v
Métricas estables
    |
    v
Estado normal
    |
    v
Sin alertas críticas
```

## 3. Sobrecarga

### Condición

Se incrementa la carga de trabajo de los servidores.

### Resultado esperado

```text
Workload ↑
    |
    v
CPU ↑
    |
    v
Consumo / temperatura ↑
    |
    v
WARNING o CRITICAL
```

## 4. Fallo de refrigeración

### Condición

Se reduce la capacidad de refrigeración.

### Resultado esperado

```text
Refrigeración ↓
    |
    v
Temperatura ↑
    |
    v
Presión ↑
    |
    v
Alerta
```

## 5. Conexión no autorizada

### Condición

Se intenta establecer una comunicación que no coincide con una regla permitida.

### Resultado esperado

```text
Conexión
    |
    v
Firewall
    |
    v
DENY
    |
    v
Evento de seguridad
    |
    v
Auditoría
```

## 6. Patrón anómalo de conexiones

El IDS incrementa el contador de conexiones para una combinación concreta de origen, destino, protocolo y puerto.

Los umbrales definidos en el módulo permiten pasar de `NORMAL` a `WARNING` y posteriormente a `CRITICAL`.

## 7. Interferencia QKD

### Condición

Se simula una interferencia en el canal.

### Resultado esperado

```text
Interferencia
      |
      v
QBER ↑
      |
      v
Sesión comprometida
      |
      v
Alerta
```

## 8. Evidencias

Para cada escenario se recomienda conservar:

- captura de pantalla;
- salida de consola;
- métricas;
- logs;
- estado antes y después;
- explicación del resultado.
