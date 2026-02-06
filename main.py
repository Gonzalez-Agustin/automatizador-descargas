import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil

# Mapeo de extensiones
EXTENSIONES = {
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Documentos': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv', '.pptx'],
    'Instaladores': ['.exe', '.msi', '.iso'],
    'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Video': ['.mp4', '.mkv', '.avi', '.mov']
}

def organizar_archivo(ruta_archivo):
    
    nombre_archivo = os.path.basename(ruta_archivo)
    if nombre_archivo.startswith('.') or nombre_archivo in ['main.py', 'README.md', 'historial.log', 'requirements.txt']: 
        return
        
    nombre, extension = os.path.splitext(nombre_archivo)
    extension = extension.lower()
    
    carpeta_destino = 'Otros'
    
    for carpeta, extensiones_validas in EXTENSIONES.items():
        if extension in extensiones_validas:
            carpeta_destino = carpeta
            break
            
    # Crear carpeta si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        
    destino = os.path.join(carpeta_destino, nombre_archivo)
    
    # Manejar duplicados
    contador = 1
    while os.path.exists(destino):
        nuevo_nombre = f"{nombre}_{contador}{extension}"
        destino = os.path.join(carpeta_destino, nuevo_nombre)
        contador += 1
        
    try:
        shutil.move(ruta_archivo, destino)
        logging.info(f"Movido: {nombre_archivo} -> {carpeta_destino}")
        print(f"✅ Movido: {nombre_archivo} a carpeta {carpeta_destino}")
    except Exception as e:
        logging.error(f"Error moviendo {nombre_archivo}: {e}")

class ManejadorDeArchivos(FileSystemEventHandler):
    def on_created(self, evento):
        if evento.is_directory:
            return
        
        # Esperar un poco para asegurar que el archivo se escriba completo
        time.sleep(1) 
        organizar_archivo(evento.src_path)

if __name__ == "__main__":
    ruta_monitoreo = "." # Monitorear directorio actual
    
    # Configurar logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='historial.log') # Guardar logs en archivo

    manejador = ManejadorDeArchivos()
    observador = Observer()
    observador.schedule(manejador, ruta_monitoreo, recursive=False)
    observador.start()
    
    print(f"👀 Monitoreando descargas en: {os.path.abspath(ruta_monitoreo)}")
    print("Presiona Ctrl+C para detener.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observador.stop()
        print("\n🛑 Deteniendo monitor...")
    observador.join()
