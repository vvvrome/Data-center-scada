# Red y conectividad del laboratorio

## 1. Introducción

DataCenter_Lab utiliza Tailscale como red privada VPN para conectar los diferentes componentes del laboratorio.

El objetivo principal es mantener la conectividad entre los sistemas independientemente de la red local utilizada. Esto permite cambiar de red Wi-Fi o ubicación sin tener que modificar continuamente las direcciones utilizadas por los servicios del laboratorio.

La VPN se utiliza principalmente para la comunicación entre:

- Kali Linux: pruebas de seguridad y pentesting.
- Windows DataCenter_Lab: servidor de la aplicación Flask y entorno SCADA.
- Ubuntu Wazuh: servidor Wazuh Manager.

---

## 2. Arquitectura de red

La arquitectura de comunicación mediante Tailscale es:

```text
                         TAILSCALE
                       Red privada VPN
                              |
             +----------------+----------------+
             |                                 |
             v                                 v
     +------------------+              +------------------+
     |      Kali        |              | Ubuntu Wazuh    |
     |    Pentesting    |              |  Wazuh Manager  |
     +------------------+              +------------------+
             |                                 ^
             |                                 |
             |          Tailscale              |
             |                                 |
             +--------------+------------------+
                            |
                            v
                   +------------------+
                   | DataCenter_Lab   |
                   |     Windows      |
                   |   Flask / SCADA  |
                   +------------------+
```

La comunicación entre los equipos se realiza mediante las direcciones privadas asignadas por Tailscale.

---

## 3. Equipos conectados

| Equipo | Sistema operativo | Función | IP Tailscale |
|---|---|---|---|
| DataCenter_Lab | Windows 10 | Aplicación Flask / SCADA | `100.x.x.x` |
| Wazuh | Ubuntu | Wazuh Manager | `100.x.x.x` |
| Kali | Kali Linux | Pentesting | `100.x.x.x` |

Las direcciones IP de Tailscale se utilizan para la comunicación privada entre los equipos del laboratorio.

Las direcciones concretas pueden cambiar en función de la configuración de Tailscale y no se incluyen en la documentación pública del repositorio.

---

## 4. Motivo del uso de Tailscale

La red local puede cambiar cuando los equipos se conectan a diferentes redes.

Por ejemplo, Windows puede obtener diferentes direcciones IP dependiendo de la red:

```text
Red 1 → 192.168.5.x
Red 2 → 192.168.1.x
Red 3 → 10.0.0.x
```

Esto puede dificultar la comunicación entre los diferentes componentes del laboratorio si los servicios dependen directamente de las direcciones IP locales.

Para solucionar este problema se utiliza Tailscale.

Cada dispositivo conectado a la red privada dispone de una dirección IP de Tailscale que permite mantener la comunicación entre los equipos aunque cambie la red local.

Ejemplo:

```text
Windows DataCenter_Lab
IP local:       variable
IP Tailscale:   100.x.x.x

Ubuntu Wazuh
IP local:       variable
IP Tailscale:   100.x.x.x
```

De esta forma, el agente Wazuh puede utilizar la dirección Tailscale del servidor Wazuh en lugar de depender de la dirección IP proporcionada por la red local.

---

## 5. Instalación

### 5.1. Windows

Tailscale se instala mediante el cliente oficial para Windows.

Después de instalarlo, el equipo se autentica utilizando la misma cuenta de Tailscale utilizada por el resto de dispositivos del laboratorio.

Para comprobar el estado de la conexión:

```powershell
tailscale status
```

Para obtener la dirección IP asignada por Tailscale:

```powershell
tailscale ip
```

---

### 5.2. Ubuntu Wazuh

En Ubuntu se instala Tailscale mediante:

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

Después se inicia Tailscale y se realiza la autenticación:

```bash
sudo tailscale up
```

Para obtener la dirección IP asignada:

```bash
tailscale ip
```

Para comprobar los dispositivos conectados:

```bash
tailscale status
```

---

### 5.3. Kali Linux

En Kali Linux se utiliza el mismo procedimiento:

```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

Después:

```bash
sudo tailscale up
```

Para comprobar la conexión:

```bash
tailscale status
```

Y para obtener la dirección IP:

```bash
tailscale ip
```

---

## 6. Configuración del agente Wazuh

El agente Wazuh instalado en Windows se configura para conectarse al Wazuh Manager mediante la dirección IP de Tailscale.

El archivo de configuración se encuentra en:

```text
C:\Program Files (x86)\ossec-agent\ossec.conf
```

La configuración utiliza la dirección Tailscale del servidor Wazuh:

```xml
<client>
    <server>
        <address>IP_TAILSCALE_WAZUH</address>
    </server>
</client>
```

Por ejemplo:

```xml
<client>
    <server>
        <address>100.x.x.x</address>
    </server>
</client>
```

Después de modificar la configuración se reinicia el servicio del agente:

```powershell
Restart-Service WazuhSvc
```

Para comprobar que el servicio está funcionando:

```powershell
Get-Service WazuhSvc
```

El servicio debe aparecer con estado:

```text
Running
```

---

## 7. Comprobación de conectividad

Una vez instalados los tres dispositivos, se comprobó la conectividad mediante Tailscale.

### 7.1. Desde Windows hacia Ubuntu

Desde Windows se utilizó:

```powershell
tailscale ping IP_TAILSCALE_WAZUH
```

También se comprobó mediante ICMP:

```powershell
ping IP_TAILSCALE_WAZUH
```

Las pruebas fueron satisfactorias.

---

### 7.2. Desde Ubuntu hacia Windows

Desde Ubuntu se utilizó:

```bash
tailscale ping IP_TAILSCALE_WINDOWS
```

También:

```bash
ping IP_TAILSCALE_WINDOWS
```

Las pruebas fueron satisfactorias.

---

## 8. Comprobación de la conexión Wazuh

El Wazuh Manager recibe las conexiones de los agentes mediante el puerto:

```text
1514
```

La conexión entre Windows y Wazuh se comprobó desde Ubuntu mediante:

```bash
sudo ss -tnp | grep 1514
```

Se obtuvo una conexión TCP establecida entre la dirección Tailscale de Ubuntu y la dirección Tailscale de Windows.

La conexión observada fue equivalente a:

```text
Ubuntu Wazuh
100.x.x.x:1514
        |
        | Wazuh Agent
        |
Windows DataCenter_Lab
100.x.x.x:xxxxx
```

Esto confirmó que el agente de Windows estaba conectado al Wazuh Manager mediante Tailscale.

---

## 9. Prueba de cambio de red

Para comprobar que la configuración no depende de una red local concreta, se realizó una prueba cambiando Windows DataCenter_Lab a otra red.

Antes del cambio:

```text
Windows DataCenter_Lab
IP local:       variable
IP Tailscale:   100.123.140.2
```

Después de cambiar de red, la dirección IP local de Windows cambió.

La dirección de Tailscale continuó siendo:

```text
100.123.140.2
```

Posteriormente se comprobó de nuevo la conectividad:

```powershell
tailscale status
```

```powershell
tailscale ping IP_TAILSCALE_WAZUH
```

Las pruebas continuaron funcionando correctamente.

---

## 10. Comprobación del funcionamiento de Wazuh después del cambio

Después de cambiar la red de Windows se comprobó que el agente Wazuh continuaba conectado al Manager.

En Ubuntu se comprobó la conexión mediante:

```bash
sudo ss -tnp | grep 1514
```

También se generó un evento de seguridad desde DataCenter_Lab.

El evento fue recibido correctamente por Wazuh y apareció en:

```text
/var/ossec/logs/alerts/alerts.json
```

Esto confirmó que el cambio de red no interrumpió la comunicación entre DataCenter_Lab y Wazuh.

---

## 11. Flujo de comunicación

El flujo de comunicación utilizado en el laboratorio es:

```text
                  TAILSCALE VPN
                       |
                       |
       +---------------+---------------+
       |                               |
       v                               v
+--------------+                +--------------+
| DataCenter   |                |    Kali      |
|    Lab       |                |  Pentesting  |
|   Windows    |                +--------------+
+------+-------+
       |
       | security.log
       |
       v
+--------------+
| Wazuh Agent  |
+------+-------+
       |
       | Tailscale
       |
       | TCP 1514
       v
+--------------+
| Wazuh Manager|
|    Ubuntu    |
+------+-------+
       |
       v
+--------------+
|    Wazuh     |
|    Alerts    |
+--------------+
```

DataCenter_Lab genera eventos de seguridad que son registrados en `security.log`.

El agente Wazuh monitoriza estos eventos y los envía al Wazuh Manager mediante la red privada Tailscale.

Wazuh procesa los eventos y genera las alertas correspondientes según las reglas configuradas.

---

## 12. Ventajas de la configuración

El uso de Tailscale proporciona varias ventajas para el laboratorio:

- Permite mantener la comunicación entre los dispositivos aunque cambie la red local.
- Evita depender de direcciones IP locales estáticas.
- Permite conectar equipos que se encuentran en diferentes redes.
- Proporciona una red privada entre los dispositivos autorizados.
- Facilita el acceso de Kali al entorno de laboratorio.
- Permite mantener la comunicación entre el agente Wazuh y el Manager cuando cambia la red utilizada por Windows.
- Evita la necesidad de exponer directamente los servicios del laboratorio a Internet.

---

## 13. Relación con la seguridad del laboratorio

Tailscale proporciona la conectividad privada entre los sistemas, pero no sustituye las medidas de seguridad implementadas en DataCenter_Lab.

La aplicación mantiene diferentes mecanismos de protección:

- Autenticación de usuarios.
- Control de acceso basado en roles.
- Protección CSRF.
- Rate limiting.
- Registro de auditoría.
- Cabeceras de seguridad.
- Content Security Policy (CSP).
- Monitorización mediante Wazuh.
- File Integrity Monitoring (FIM).
- Reglas personalizadas de detección en Wazuh.

La VPN se utiliza como una capa adicional de conectividad y aislamiento de la infraestructura.

---

## 14. Seguridad de la configuración

Las direcciones IP privadas de Tailscale y otros datos específicos de la infraestructura no se almacenan directamente en el repositorio público.

La configuración específica de cada equipo se mantiene en la propia máquina.

No se deben almacenar en GitHub:

- Credenciales.
- Claves privadas.
- Tokens de autenticación.
- Archivos `.env`.
- Configuraciones sensibles.
- Información innecesaria sobre la infraestructura privada.

---

## 15. Resultado final

La arquitectura final del laboratorio permite mantener una comunicación estable entre los diferentes sistemas independientemente de la red local utilizada.

```text
                         TAILSCALE
                      RED PRIVADA VPN
                             |
          +------------------+------------------+
          |                  |                  |
          v                  v                  v
     +---------+       +-----------+      +-----------+
     |  Kali   |       | DataCenter|      |  Ubuntu   |
     |         |       |    Lab    |      |   Wazuh   |
     |Pentest  |       |  Windows  |      |  Manager  |
     +---------+       +-----+-----+      +-----+-----+
                             |                  ^
                             |                  |
                             | Wazuh Agent      |
                             +------------------+
                                TCP 1514
```

La prueba de cambio de red confirmó que:

1. La dirección IP local de Windows puede cambiar.
2. La conexión Tailscale permanece disponible.
3. Windows continúa comunicándose con Ubuntu mediante la red privada.
4. El agente Wazuh continúa conectado al Wazuh Manager.
5. Los eventos generados por DataCenter_Lab continúan llegando a Wazuh.
6. Las alertas de seguridad continúan funcionando correctamente.

Por tanto, la conectividad del laboratorio queda desacoplada de la red local utilizada por los dispositivos.