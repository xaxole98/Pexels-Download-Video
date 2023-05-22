# Script para definir la carpeta de destino

# Importa params desde verify_parameters
from verify_parameters import params
import os

def get_save_folder():
    """Función para obtener la carpeta de destino para los videos y fotos descargados de Pexels"""
    save_folder = params.save
    media_type = params.media_type
    query = params.query

    # Crea una nueva carpeta en la ruta obtenida
    if not os.path.exists(os.path.join(save_folder, f"{media_type}_{query}")):
        os.makedirs(os.path.join(save_folder, f"{media_type}_{query}"))

    # Asigna la nueva carpeta como la carpeta de destino para los videos y fotos descargados de Pexels
    save_folder = os.path.join(save_folder, f"{media_type}_{query}")

    return save_folder
