# DataCenter Lab

Laboratorio de simulación de infraestructura crítica desarrollado en Python.

DataCenter Lab es un entorno de experimentación que integra la simulación de una infraestructura de centro de datos con sistemas de monitorización, seguridad informática, arquitectura IT/OT, una planta nuclear simplificada, análisis matemático y una simulación educativa de comunicaciones cuánticas.

El proyecto tiene como finalidad estudiar el comportamiento de diferentes componentes de una infraestructura crítica y analizar cómo interactúan los sistemas informáticos, las redes, los procesos físicos y los mecanismos de seguridad.

---

## Índice

* [Descripción](#descripción)
* [Objetivos](#objetivos)
* [Características](#características)
* [Arquitectura](#arquitectura)
* [Estructura del proyecto](#estructura-del-proyecto)
* [Módulos principales](#módulos-principales)
* [Infraestructura del datacenter](#infraestructura-del-datacenter)
* [Motor de simulación](#motor-de-simulación)
* [Monitorización](#monitorización)
* [Ciberseguridad](#ciberseguridad)
* [Arquitectura IT/OT](#arquitectura-itot)
* [Simulación de planta nuclear](#simulación-de-planta-nuclear)
* [Modelos físicos y matemáticos](#modelos-físicos-y-matemáticos)
* [Graph Lab](#graph-lab)
* [Simulación QKD](#simulación-qkd)
* [API y aplicación web](#api-y-aplicación-web)
* [Base de datos](#base-de-datos)
* [Configuración](#configuración)
* [Instalación](#instalación)
* [Ejecución](#ejecución)
* [Testing](#testing)
* [Escenarios de prueba](#escenarios-de-prueba)
* [Documentación](#documentación)
* [Limitaciones](#limitaciones)
* [Trabajo futuro](#trabajo-futuro)
* [Tecnologías utilizadas](#tecnologías-utilizadas)
* [Autor](#autor)

---

# Descripción

DataCenter Lab nace como un proyecto de simulación de infraestructura informática y evoluciona hacia un laboratorio más amplio orientado a sistemas críticos.

El proyecto combina diferentes áreas:

```text
                    DataCenter Lab
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
     Datacenter        Seguridad        Graph Lab
          │               │                │
          ▼               ▼                ▼
     Simulación       IT / OT          Matemáticas
          │               │                │
          └───────────────┼────────────────┘
                          │
                          ▼
                  Infraestructura
                      crítica
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
        Planta simulada              QKD
```

El objetivo no es reproducir una instalación real con precisión de ingeniería, sino proporcionar un entorno controlado en el que estudiar conceptos relacionados con sistemas, redes, seguridad, monitorización, física y matemáticas.

---

# Objetivos

## Objetivo general

Desarrollar un laboratorio software capaz de simular, monitorizar y analizar una infraestructura tecnológica asociada a sistemas críticos, integrando componentes IT, OT, seguridad y modelos físicos y matemáticos.

## Objetivos específicos

* Modelar una infraestructura de centro de datos.
* Simular servidores y dispositivos de red.
* Modelar racks y componentes de infraestructura.
* Generar cargas de trabajo.
* Simular consumo energético.
* Simular procesos de refrigeración.
* Monitorizar diferentes métricas.
* Detectar estados normales y anómalos.
* Generar alertas.
* Implementar autenticación de usuarios.
* Implementar diferentes roles de acceso.
* Registrar eventos mediante auditoría.
* Simular reglas de firewall.
* Implementar un sistema IDS.
* Representar una arquitectura IT/OT.
* Simular una planta nuclear simplificada.
* Modelar sensores y actuadores.
* Introducir fallos controlados.
* Implementar mecanismos de seguridad para la planta.
* Simular el protocolo BB84/QKD.
* Analizar el QBER.
* Integrar Graph Lab.
* Representar funciones matemáticas.
* Analizar datos mediante gráficas.
* Estudiar simulaciones orbitales.
* Crear una interfaz web para interactuar con el laboratorio.

---

# Características

### Infraestructura

* Datacenter virtual.
* Racks.
* Servidores.
* Switches.
* Routers.
* Sistemas de almacenamiento.
* Sistemas de alimentación.

### Simulación

* Generación de carga de trabajo.
* Variación de recursos.
* Consumo energético.
* Refrigeración.
* Tráfico de red.
* Simulación de fallos.
* Actualización periódica del estado del sistema.

### Monitorización

* CPU.
* RAM.
* Temperatura.
* Consumo.
* Tráfico.
* Estado de dispositivos.
* Alertas.
* Logs.

### Seguridad

* Autenticación.
* Autorización.
* Roles.
* Protección CSRF.
* Rate limiting.
* Cookies seguras.
* Cabeceras de seguridad.
* Firewall.
* IDS.
* Auditoría.

### Sistemas críticos

* Planta nuclear simplificada.
* Reactor.
* Sensores.
* Actuadores.
* Controlador.
* Gestión de fallos.
* Control de seguridad.
* Alertas.

### Matemáticas y física

* Funciones matemáticas.
* Series.
* Análisis de datos.
* Representación gráfica.
* Simulación orbital.
* Modelos físicos simplificados.

### Criptografía

* Simulación BB84.
* QKD.
* Canal cuántico.
* QBER.
* Detección de interferencias.
* Gestión de sesiones.

---

# Arquitectura

La arquitectura general del proyecto se puede representar de la siguiente manera:

```text
                         Usuario
                            │
                            ▼
                   ┌─────────────────┐
                   │  Aplicación Web │
                   │     Flask       │
                   └────────┬────────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
       ┌───────────┐  ┌───────────┐  ┌───────────┐
       │DataCenter │  │ Seguridad │  │ Graph Lab │
       │   Lab     │  │           │  │           │
       └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
             │              │              │
             ▼              ▼              ▼
       Infraestructura   Firewall      Matemáticas
             │              │          y gráficas
             ▼              ▼
       Motor de          IDS
       simulación          │
             │              ▼
             ▼          Auditoría
       Monitorización
             │
             ▼
          Alertas
             │
             ▼
       ┌───────────────┐
       │    Planta     │
       │    crítica    │
       └───────┬───────┘
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
    Reactor  Sensores  Actuadores
               │
               ▼
          Seguridad OT
               │
               ▼
              QKD
```

La aplicación está organizada de forma modular para separar la lógica de infraestructura, simulación, monitorización, seguridad, planta, análisis matemático y presentación web.

---

# Estructura del proyecto

```text
integrated/
│
├── API/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── config/
│   ├── datacenter.yaml
│   └── loader.py
│
├── database/
│   ├── users.py
│   ├── audit.py
│   └── create_admin.py
│
├── graph_lab/
│   ├── expression_parser.py
│   ├── plotting.py
│   ├── routes.py
│   ├── security.py
│   ├── templates/
│   └── static/
│
├── infraestructura/
│   ├── datacenter.py
│   ├── rack.py
│   ├── server.py
│   ├── switch.py
│   ├── router.py
│   ├── storage.py
│   └── ups.py
│
├── monitorizar/
│   ├── metrics.py
│   ├── logs.py
│   └── alerts.py
│
├── planta/
│   ├── reactor.py
│   ├── sensors.py
│   ├── actuators.py
│   ├── controller.py
│   ├── faults.py
│   ├── safety.py
│   └── ...
│
├── seguridad/
│   ├── firewall.py
│   ├── ids.py
│   └── ...
│
├── simulacion/
│   ├── motor.py
│   ├── workload.py
│   ├── power.py
│   ├── cooler.py
│   ├── network.py
│   └── failures.py
│
├── tests/
│   ├── test_qkd.py
│   └── test_qkd_manager.py
│
├── docs/
│   ├── arquitectura.md
│   ├── infraestructura.md
│   ├── simulacion.md
│   ├── monitorizacion.md
│   ├── seguridad.md
│   ├── planta.md
│   ├── fisica.md
│   ├── qkd.md
│   ├── graph_lab.md
│   ├── api.md
│   ├── base_datos.md
│   ├── configuracion.md
│   ├── testing.md
│   ├── escenarios.md
│   ├── limitaciones.md
│   └── futuro.md
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Módulos principales

## API

Contiene la aplicación Flask y actúa como punto de comunicación entre los modelos internos y la interfaz web.

Gestiona:

* rutas.
* autenticación.
* sesiones.
* usuarios.
* administración.
* acceso a datos del laboratorio.
* Graph Lab.

---

## Config

Contiene la configuración del laboratorio.

La infraestructura puede definirse mediante archivos YAML y posteriormente cargarse en los objetos Python.

```text
datacenter.yaml
       │
       ▼
    loader.py
       │
       ▼
   DataCenter
       │
       ▼
Infraestructura
```

---

## Database

Gestiona la información persistente relacionada con:

* usuarios.
* roles.
* auditoría.

El proyecto utiliza SQLite para el laboratorio.

---

## Infraestructura

Representa los elementos físicos y lógicos del centro de datos.

```text
DataCenter
    │
    └── Rack
          ├── Server
          ├── Switch
          ├── Router
          └── Storage
```

---

## Monitorización

Recopila y procesa información sobre el estado del sistema.

Puede trabajar con métricas como:

* CPU.
* RAM.
* temperatura.
* consumo.
* tráfico.
* estado.

Las condiciones anómalas pueden generar alertas.

---

## Planta

Contiene la simulación de una planta nuclear simplificada.

El módulo representa:

* reactor.
* sensores.
* actuadores.
* controlador.
* fallos.
* seguridad.
* alertas.
* comunicaciones.

---

## Seguridad

Contiene mecanismos relacionados con la seguridad del laboratorio.

Entre ellos:

* firewall.
* IDS.
* reglas de comunicación.
* detección de eventos.
* registro de eventos.

---

## Simulación

Contiene el motor que actualiza periódicamente el estado del laboratorio.

El ciclo de simulación puede representarse como:

```text
Actualizar planta
       ↓
Generar workload
       ↓
Actualizar servidores
       ↓
Actualizar red
       ↓
Actualizar consumo
       ↓
Comprobar estados
       ↓
Generar alertas
       ↓
Siguiente ciclo
```

---

# Infraestructura del datacenter

La infraestructura se modela mediante diferentes objetos Python.

## Servidores

Los servidores pueden tener diferentes métricas:

* CPU.
* RAM.
* almacenamiento.
* temperatura.
* consumo.
* tráfico.
* estado.

## Racks

Los racks representan la distribución física de los dispositivos.

Se tienen en cuenta elementos como:

* capacidad.
* unidades utilizadas.
* dispositivos instalados.

## Switches

Se pueden representar características relacionadas con:

* puertos.
* tráfico.
* utilización.
* temperatura.
* consumo.

## Routers

Representan elementos de conectividad y encaminamiento dentro de la infraestructura.

---

# Motor de simulación

El motor de simulación permite que el laboratorio no sea un conjunto estático de objetos, sino un entorno dinámico.

Durante cada ciclo se actualizan diferentes variables del sistema.

Por ejemplo:

```text
Workload ↑
    │
    ├── CPU ↑
    ├── consumo ↑
    └── temperatura ↑
```

La modificación de estas variables puede provocar cambios de estado y generación de alertas.

---

# Monitorización

Los componentes monitorizados pueden presentar diferentes estados:

```text
        NORMAL
           │
           ▼
        WARNING
           │
           ▼
        CRITICAL
```

El sistema de alertas tiene en cuenta la persistencia de determinadas condiciones para evitar que una fluctuación puntual genere inmediatamente una alerta.

Las alertas y eventos pueden quedar registrados para su posterior análisis.

---

# Ciberseguridad

DataCenter Lab incorpora seguridad tanto en la aplicación web como en la infraestructura simulada.

## Seguridad web

Entre los mecanismos utilizados se encuentran:

* Protección CSRF.
* Rate limiting.
* Cookies HttpOnly.
* SameSite.
* Content Security Policy.
* X-Frame-Options.
* X-Content-Type-Options.
* Referrer-Policy.
* Permissions-Policy.

## Autenticación

La aplicación permite:

* registro de usuarios.
* inicio de sesión.
* cierre de sesión.
* gestión de sesiones.

## Roles

Se utilizan diferentes niveles de acceso.

```text
Usuario
  │
  ├── VIEWER
  │
  └── ADMIN
```

El administrador dispone de funcionalidades adicionales relacionadas con usuarios y auditoría.

## Auditoría

Las acciones relevantes pueden quedar registradas.

Ejemplos:

```text
LOGIN
LOGOUT
REGISTER
ACCESS_ADMIN_USERS
ACCESS_AUDIT_LOG
CSRF_BLOCKED
FIREWALL_DENY
```

---

# Arquitectura IT/OT

Uno de los objetivos del proyecto es representar de forma simplificada la separación entre sistemas IT y OT.

```text
              IT
               │
               ▼
              DMZ
               │
               ▼
               OT
               │
               ▼
            CONTROL
               │
               ▼
          Proceso físico
```

La comunicación entre diferentes zonas se controla mediante reglas de firewall.

Por ejemplo:

```text
DMZ → OT
TCP/443
ALLOW
```

o:

```text
OT → CONTROL
TCP/502
ALLOW
```

Las conexiones no permitidas pueden generar eventos de seguridad.

---

# Simulación de planta nuclear

El proyecto incorpora una representación simplificada de una planta nuclear con finalidad educativa.

La arquitectura contiene:

```text
NuclearPlant
│
├── Reactor
├── Sensors
├── Actuators
├── PlantController
├── FaultManager
├── SafetyController
├── PlantAlertManager
│
└── Security
    ├── SecurityController
    ├── IntrusionDetector
    ├── QKDManager
    ├── QuantumChannel
    └── QKD
```

## Reactor

El reactor utiliza variables simplificadas como:

* temperatura.
* presión.
* caudal.
* potencia.
* nivel de agua.
* radiación.

## Sensores

Los sensores permiten obtener información sobre el estado del proceso.

## Actuadores

Los actuadores permiten modificar determinadas variables de la simulación.

## Control

El controlador utiliza la información proporcionada por los sensores para gestionar el comportamiento del sistema.

## Fallos

El sistema permite introducir condiciones de fallo para estudiar la respuesta de los mecanismos de monitorización y seguridad.

---

# Modelos físicos y matemáticos

El proyecto utiliza modelos físicos simplificados para representar la evolución de determinadas variables.

Una aproximación conceptual del comportamiento térmico es:

```text
Generación de calor
        -
Refrigeración
        =
Variación térmica
```

De forma simplificada:

$$
\Delta T \propto Q_{generado} - Q_{refrigerado}
$$

Por tanto:

```text
Potencia ↑
   ↓
Calor generado ↑
   ↓
Temperatura ↑
   ↓
Presión ↑
```

Mientras que:

```text
Refrigeración ↑
   ↓
Eliminación de calor ↑
   ↓
Temperatura ↓
```

Estos modelos permiten estudiar la relación entre diferentes variables y analizar el comportamiento dinámico del sistema.

---

# Graph Lab

Graph Lab es el componente matemático y gráfico integrado en DataCenter Lab.

Originalmente se desarrolló como un proyecto independiente y posteriormente se incorporó al laboratorio.

Sus principales funcionalidades incluyen:

* representación de funciones.
* generación de series.
* análisis de datos.
* representación gráfica.
* simulación orbital.

Ejemplos de funciones:

$$
y=x
$$

$$
y=x^2
$$

$$
y=x^3
$$

La integración permite utilizar Graph Lab como herramienta de análisis de datos generados por el laboratorio.

---

# Simulación orbital

Graph Lab incorpora funcionalidades relacionadas con simulaciones orbitales.

Esta parte del proyecto permite estudiar conceptos relacionados con:

* movimiento orbital.
* integración numérica.
* sistemas dinámicos.
* problema de tres cuerpos.
* estabilidad.
* representación de trayectorias.

Como evolución del proyecto se plantea ampliar esta parte para estudiar:

* sistema Sol-Tierra-Luna.
* integración Leapfrog.
* puntos de Lagrange.
* secciones de Poincaré.
* estabilidad orbital.

---

# Simulación QKD

DataCenter Lab incluye una simulación educativa de distribución cuántica de claves basada en el protocolo BB84.

La arquitectura conceptual es:

```text
Alice
  │
  ▼
Canal cuántico
  │
  ▼
 Bob
  │
  ▼
QKD Manager
```

El sistema permite simular:

* bits.
* bases.
* mediciones.
* comparación de bases.
* generación de clave.
* QBER.
* interferencias.

## QBER

QBER representa la tasa de error de bits cuánticos.

Dentro de la simulación se utiliza para analizar el estado de la comunicación:

```text
QBER bajo
    ↓
Comunicación normal
```

y:

```text
QBER elevado
    ↓
Posible interferencia
    ↓
Estado comprometido
    ↓
Alerta
```

El sistema mantiene información sobre:

* sesiones.
* sesiones exitosas.
* sesiones comprometidas.
* QBER.
* historial.
* longitud de clave.
* estado del canal.

La implementación tiene finalidad educativa y no representa un sistema QKD físico.

---

# API y aplicación web

La aplicación web está desarrollada mediante Flask.

El flujo general es:

```text
Modelo Python
      ↓
Flask
      ↓
API / rutas
      ↓
HTML / JSON
      ↓
JavaScript / Jinja2
      ↓
Navegador
```

La aplicación proporciona funcionalidades relacionadas con:

* autenticación.
* registro.
* sesiones.
* dashboard.
* administración.
* auditoría.
* monitorización.
* planta.
* Graph Lab.

---

# Base de datos

El proyecto utiliza SQLite para almacenar información persistente.

La estructura principal se encuentra en:

```text
database/
├── users.py
├── audit.py
└── create_admin.py
```

La base de datos contiene información relacionada con usuarios y auditoría.

Los datos sensibles y credenciales no deben almacenarse directamente en el repositorio.

---

# Configuración

La infraestructura del datacenter puede configurarse mediante:

```text
config/datacenter.yaml
```

El archivo de configuración se carga mediante:

```text
datacenter.yaml
       ↓
loader.py
       ↓
DataCenter
```

Separar la configuración del código permite modificar determinados parámetros de la infraestructura sin tener que modificar las clases Python.

---

# Instalación

## Requisitos

Se recomienda utilizar:

* Python 3.
* Git.
* pip.
* entorno virtual de Python.

## Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd DataCenter_Lab/integrated
```

## Crear entorno virtual

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Configuración de variables de entorno

La clave secreta de Flask debe proporcionarse mediante una variable de entorno.

Linux:

```bash
export FLASK_SECRET_KEY="tu_clave_secreta"
```

Windows PowerShell:

```powershell
$env:FLASK_SECRET_KEY="tu_clave_secreta"
```

No se deben almacenar claves secretas directamente en Git.

---

# Ejecución

Una vez instaladas las dependencias:

```bash
python main.py
```

La aplicación Flask iniciará el laboratorio.

El acceso se realizará mediante la dirección local indicada por Flask.

---

# Testing

Las pruebas automatizadas se encuentran en:

```text
tests/
├── test_qkd.py
└── test_qkd_manager.py
```

Las pruebas pueden ejecutarse mediante:

```bash
pytest
```

Actualmente las pruebas se concentran especialmente en los componentes relacionados con QKD.

Como evolución se plantea ampliar la cobertura hacia:

* infraestructura.
* monitorización.
* firewall.
* IDS.
* autenticación.
* API.
* planta.
* simulación.

---

# Escenarios de prueba

El laboratorio permite plantear diferentes escenarios experimentales.

## Funcionamiento normal

```text
Carga normal
     ↓
Recursos estables
     ↓
Temperaturas normales
     ↓
Estado ONLINE
     ↓
Sin alertas críticas
```

## Sobrecarga

```text
Workload ↑
     ↓
CPU ↑
     ↓
Temperatura ↑
     ↓
WARNING
     ↓
Alerta si persiste
```

## Fallo de refrigeración

```text
Refrigeración ↓
     ↓
Temperatura ↑
     ↓
Presión ↑
     ↓
WARNING / CRITICAL
     ↓
Sistema de seguridad
```

## Comunicación no autorizada

```text
Conexión
    ↓
Firewall
    ↓
Comprobación de reglas
    │
    ├── ALLOW
    │
    └── DENY
          ↓
    Evento de seguridad
```

## Interferencia en QKD

```text
Alice
  ↓
Canal
  ↓
Interferencia
  ↓
Bob
  ↓
QBER ↑
  ↓
Estado comprometido
  ↓
Alerta
```

---

# Documentación

La documentación técnica ampliada se encuentra en la carpeta `docs/`.

| Documento                                  | Contenido                            |
| ------------------------------------------ | ------------------------------------ |
| [Arquitectura](docs/arquitectura.md)       | Arquitectura general del sistema     |
| [Infraestructura](docs/infraestructura.md) | Servidores, racks y dispositivos     |
| [Simulación](docs/simulacion.md)           | Motor y comportamiento dinámico      |
| [Monitorización](docs/monitorizacion.md)   | Métricas y alertas                   |
| [Seguridad](docs/seguridad.md)             | Seguridad web e infraestructura      |
| [Planta](docs/planta.md)                   | Simulación de planta crítica         |
| [Física](docs/fisica.md)                   | Modelos físicos y matemáticos        |
| [QKD](docs/qkd.md)                         | Simulación BB84/QKD                  |
| [Graph Lab](docs/graph_lab.md)             | Análisis y representación matemática |
| [API](docs/api.md)                         | Aplicación web y API                 |
| [Base de datos](docs/base_datos.md)        | Usuarios y auditoría                 |
| [Configuración](docs/configuracion.md)     | Configuración YAML                   |
| [Testing](docs/testing.md)                 | Pruebas automatizadas                |
| [Escenarios](docs/escenarios.md)           | Escenarios experimentales            |
| [Limitaciones](docs/limitaciones.md)       | Limitaciones actuales                |
| [Trabajo futuro](docs/futuro.md)           | Evolución prevista                   |

---

# Limitaciones

DataCenter Lab es un laboratorio de simulación y experimentación.

## Modelos físicos

Los modelos físicos son simplificaciones destinadas al aprendizaje y la experimentación computacional.

## Planta nuclear

La planta simulada no representa una instalación nuclear real ni debe utilizarse para diseñar, controlar o evaluar una instalación de este tipo.

## Redes

Los dispositivos de red se representan mediante modelos software y no mediante hardware industrial real.

## QKD

La implementación QKD es una simulación educativa del protocolo y no una implementación de hardware cuántico.

## Base de datos

SQLite resulta adecuada para el laboratorio, aunque un despliegue de mayor escala podría utilizar otro sistema de base de datos.

## Testing

La cobertura de pruebas todavía es parcial y se encuentra en desarrollo.

## Escalabilidad

El proyecto está orientado principalmente a entornos de experimentación local.

---

# Trabajo futuro

El proyecto está diseñado para poder ampliarse progresivamente.

## Wazuh

Integración con Wazuh para:

* centralización de logs.
* detección de anomalías.
* correlación de eventos.
* generación de alertas.
* monitorización de seguridad.

## IT/OT

Ampliación de la simulación de:

* redes IT.
* DMZ.
* redes OT.
* sistemas de control.
* dispositivos industriales.

## Física

Ampliación de los modelos mediante:

* integración numérica.
* modelos térmicos más completos.
* problema de tres cuerpos.
* sistema Sol-Tierra-Luna.
* integración Leapfrog.
* puntos de Lagrange.
* secciones de Poincaré.

## Seguridad

Ampliación de:

* IDS.
* detección de anomalías.
* correlación de eventos.
* políticas IT/OT.
* auditoría.
* integración con SIEM.

## Infraestructura

Incorporación de:

* redundancia.
* balanceo.
* alta disponibilidad.
* más dispositivos.
* escenarios de fallo.
* almacenamiento avanzado.

## Despliegue

Estudio del despliegue mediante:

* Docker.
* Linux.
* máquinas virtuales.
* redes virtualizadas.

## Monitorización

Incorporación de almacenamiento histórico de métricas y representación temporal.

---

# Tecnologías utilizadas

## Lenguajes

* Python
* HTML
* CSS
* JavaScript
* YAML

## Frameworks y librerías

* Flask
* Jinja2
* NumPy
* SciPy
* Matplotlib
* PyYAML

## Base de datos

* SQLite

## Herramientas

* Git
* GitHub
* VS Code
* Linux

---

# Relación con ASIR

El proyecto integra conocimientos de diferentes áreas relacionadas con el ciclo de Administración de Sistemas Informáticos en Red.

| Área                 | Aplicación                                |
| -------------------- | ----------------------------------------- |
| Sistemas             | Modelado de servidores e infraestructura  |
| Redes                | Routers, switches, puertos y segmentación |
| Seguridad            | Firewall, IDS, autenticación y auditoría  |
| Bases de datos       | SQLite y gestión de usuarios              |
| Lenguaje de marcas   | HTML, YAML                                |
| Programación         | Python                                    |
| Desarrollo web       | Flask, Jinja2, JavaScript                 |
| Hardware             | Modelado de servidores y consumo          |
| Monitorización       | Métricas y alertas                        |
| Linux                | Desarrollo y despliegue                   |
| Control de versiones | Git y GitHub                              |

El proyecto también amplía estos conocimientos hacia áreas relacionadas con:

* ciberseguridad.
* sistemas industriales.
* IT/OT.
* física computacional.
* matemáticas.
* criptografía.
* infraestructuras críticas.

---

# Estado del proyecto

**Estado: En desarrollo**

El proyecto continúa evolucionando mediante la incorporación de nuevos modelos de simulación, mecanismos de seguridad, herramientas de monitorización y funcionalidades de análisis.

---

# Licencia

Este proyecto se desarrolla con fines educativos y de experimentación.

La licencia definitiva se establecerá en función de los requisitos del proyecto y del uso previsto del código.

---

# Autor

**vvvrome**

Proyecto desarrollado como laboratorio personal de experimentación en:

* Administración de Sistemas.
* Redes.
* Ciberseguridad.
* Programación.
* Sistemas IT/OT.
* Simulación física.
* Análisis matemático.

---
