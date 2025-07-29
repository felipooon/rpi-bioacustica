# Sistema de Grabación Bioacústica con Raspberry Pi

Este proyecto permite registrar sonidos de aves de manera automática usando una Raspberry Pi, un micrófono y una batería externa. Está pensado para su uso en ambientes naturales con grabaciones periódicas o activadas por sonido.

##  Requisitos
- Raspberry Pi con Raspberry Pi OS
- Micrófono lavalier o USB
- Tarjeta de sonido USB (si se requiere)
- Batería externa (opcional)
- Conexión SSH/SCP para transferencia remota

##  Instalación de dependencias

```bash
sudo apt update
sudo apt install alsa-utils sox cron openssh-client
```

##  Uso básico

### Grabación periódica

```bash
bash grabacion/grabacion.sh
```

### Activación por sonido (experimental)

```bash
bash deteccion_sonido/grabar_por_sonido.sh
```

##  Automatización con cron

Ejecuta `crontab -e` y agrega:

```cron
*/15 * * * * /home/pi/rpi-bioacustica/grabacion/grabacion.sh
```

##  Transferencia remota

Edita `transferencia/subir_scp.sh` con tu IP y ejecuta:

```bash
bash transferencia/subir_scp.sh
```

## 📄 Documentación técnica
Revisar en la carpeta `docs/`.

## 🧠 Créditos e inspiración
Basado en experiencias de monitoreo acústico y el proyecto [rpi-eco-monitoring](https://github.com/sarabsethi/rpi-eco-monitoring).
