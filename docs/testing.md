# Testing

## 1. Objetivo

El proyecto contiene pruebas automatizadas para verificar componentes relacionados principalmente con QKD.

## 2. Estructura

```text
tests/
├── test_qkd.py
└── test_qkd_manager.py
```

## 3. test_qkd.py

Comprueba el comportamiento del módulo QKD.

El objetivo es verificar que la simulación de las operaciones del protocolo funciona según las condiciones definidas por el proyecto.

## 4. test_qkd_manager.py

Comprueba el comportamiento del gestor de sesiones QKD y la información que mantiene sobre las sesiones.

## 5. Ejecución

Con las dependencias instaladas:

```bash
pytest
```

También puede utilizarse:

```bash
python -m pytest
```

## 6. Cobertura actual

La cobertura actual no incluye todos los módulos del laboratorio.

Como ampliación se plantea incorporar pruebas para:

- infraestructura;
- motor de simulación;
- monitorización;
- firewall;
- IDS;
- autenticación;
- API;
- planta;
- Graph Lab.

## 7. Objetivo futuro

La ampliación de tests permitirá detectar regresiones a medida que se incorporen nuevas funcionalidades.
