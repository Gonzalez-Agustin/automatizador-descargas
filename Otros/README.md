# 📂 Python Download Automator

> Un script inteligente que mantiene tu carpeta de descargas organizada automáticamente en tiempo real.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Terminado-success?style=for-the-badge)

## 🧐 ¿Qué es esto?

Este proyecto es una herramienta de automatización que desarrollé para solucionar el problema del "caos digital". Se ejecuta en segundo plano y monitorea una carpeta específica (como Descargas). En cuanto detecta un archivo nuevo, lo clasifica y lo mueve instantáneamente a su carpeta correspondiente según su extensión.

### ✨ Características Principales
*   **Monitoreo en Tiempo Real**: Usa la librería `watchdog` para detectar eventos del sistema de archivos al instante.
*   **Clasificación Inteligente**: Separa Imágenes, Documentos, Instaladores, Audio, Video y Comprimidos.
*   **Manejo de Conflictos**: Si un archivo ya existe, lo renombra automáticamente (ej: `foto_1.jpg`) en lugar de sobrescribirlo.
*   **Logging Completo**: Mantiene un historial detallado de todos los movimientos en `historial.log`.

## 🛠️ Tecnologías

*   **Python 3**: Lenguaje base.
*   **Watchdog API**: Para el manejo de eventos del sistema de archivos (`FileSystemEventHandler`).
*   **Shutil & OS**: Para manipulación de rutas y archivos de alto nivel.

## 🚀 Cómo probarlo

Si quieres ejecutar este proyecto en tu máquina local:

1.  **Clona el repositorio**
    ```bash
    git clone https://github.com/TU_USUARIO/download-automator.git
    cd download-automator
    ```

2.  **Crea el entorno virtual**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: .\venv\Scripts\activate
    ```

3.  **Instala las dependencias**
    ```bash
    pip install watchdog
    ```

4.  **Ejecuta el script**
    ```bash
    python main.py
    ```
    *Ahora, cualquier archivo que pegues en la carpeta del proyecto será organizado automáticamente.*

## 📸 Demo

*(Aquí puedes insertar un GIF o captura de pantalla de tu terminal funcionando)*

## 👤 Autor

**Agustín** - [Tu LinkedIn] - [Tu Portfolio]

---
*Este proyecto fue creado con fines educativos para demostrar habilidades en Scripting y Automatización con Python.*
