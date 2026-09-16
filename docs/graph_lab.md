# Graph Lab

## 1. Descripción

Graph Lab es el módulo de análisis matemático y representación gráfica integrado en DataCenter Lab.

Originalmente se desarrolló como un proyecto independiente y posteriormente se incorporó a la versión integrada.

## 2. Funcionalidades

Graph Lab dispone de secciones para:

- datos;
- tipos;
- funciones;
- series;
- análisis;
- orbital.

## 3. Estructura

```text
graph_lab/
├── expression_parser.py
├── plotting.py
├── routes.py
├── security.py
├── templates/
└── static/
```

## 4. Expression Parser

`expression_parser.py` interpreta expresiones matemáticas mediante el módulo `ast`.

Se permiten operaciones y funciones matemáticas concretas.

Entre las funciones permitidas se encuentran:

- `sin`;
- `cos`;
- `tan`;
- `sqrt`;
- `exp`;
- `log`;
- `abs`.

También se permiten las constantes `pi` y `e`.

## 5. Seguridad del parser

La expresión no se ejecuta directamente como código Python.

El parser analiza el árbol sintáctico y solo acepta nodos y operaciones expresamente permitidos.

También existen límites sobre la longitud de la expresión y los exponentes.

Esto reduce el riesgo de que la funcionalidad matemática pueda utilizarse para ejecutar operaciones Python arbitrarias.

## 6. Plotting

`plotting.py` contiene la generación de representaciones gráficas.

## 7. Integración

Las rutas de Graph Lab se integran mediante un blueprint Flask.

Esto permite utilizar las herramientas matemáticas desde la aplicación principal.
