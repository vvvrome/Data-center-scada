# Física y modelos matemáticos

## 1. Objetivo

El proyecto utiliza modelos matemáticos y físicos simplificados para representar la evolución de variables del laboratorio.

La finalidad es relacionar la programación con conceptos de física y análisis numérico.

## 2. Variables físicas

La simulación de la planta utiliza, entre otras:

- temperatura;
- presión;
- potencia;
- caudal;
- nivel de agua;
- radiación.

## 3. Modelo térmico conceptual

El comportamiento térmico puede interpretarse como una diferencia entre generación y eliminación de calor:

```text
Calor generado - Calor eliminado = Variación térmica
```

De forma conceptual:

\[
\Delta T \propto Q_{generado}-Q_{refrigerado}
\]

Por tanto, dentro del modelo:

```text
Potencia ↑
   |
   v
Calor generado ↑
   |
   v
Temperatura ↑
```

Mientras que:

```text
Refrigeración ↑
   |
   v
Calor eliminado ↑
   |
   v
Temperatura ↓
```

## 4. Análisis matemático

Graph Lab permite trabajar con funciones y series.

Ejemplos:

\[
y=x
\]

\[
y=x^2
\]

\[
y=x^3
\]

Estas funciones sirven como base para probar la generación de datos y su representación gráfica.

## 5. Simulación orbital

El proyecto también contempla una línea de trabajo relacionada con:

- movimiento orbital;
- integración numérica;
- problema de tres cuerpos;
- sistema Sol-Tierra-Luna;
- puntos de Lagrange;
- secciones de Poincaré.

## 6. Métodos numéricos previstos

Como evolución del laboratorio se plantea utilizar integración Leapfrog para determinadas simulaciones orbitales.

## 7. Limitaciones

Los modelos físicos son simplificados y tienen finalidad educativa. No deben utilizarse para representar con precisión sistemas físicos o industriales reales.
