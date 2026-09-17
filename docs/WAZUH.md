# Integración con Wazuh

## 1. Arquitectura

DataCenter_Lab se integra con Wazuh para centralizar y analizar eventos de seguridad.

```text
Windows DataCenter_Lab
        │
        │ security.log
        ▼
   Wazuh Agent
        │
        ▼
 Wazuh Manager
        │
        ▼
 Wazuh Dashboard