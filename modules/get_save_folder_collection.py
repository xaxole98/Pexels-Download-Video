import collectionurl
import requests
import os
from verify_parameters import params 

def get_save_folder_collection():
    """Función para obtener la carpeta de destino para los videos y fotos descargados de Pexels"""
    save_folder_collection = params.save
    media_type = params.media_type
    collection_url = collectionurl.collectionurl()

    # Separar la URL en partes y obtener solo el nombre de la colección
    collection_url_parts = collection_url.split("/")
    collection_name = collection_url_parts[-2]

    # Crea una nueva carpeta en la ruta obtenida
    if not os.path.exists(os.path.join(save_folder_collection, f"{media_type}_{collection_name}")):
        os.makedirs(os.path.join(save_folder_collection, f"{media_type}_{collection_name}"))

    # Asigna la nueva carpeta como la carpeta de destino para los videos y fotos descargados de Pexels
    save_folder_collection = os.path.join(save_folder_collection, f"{media_type}_{collection_name}")

    return save_folder_collection

get_save_folder_collection()
