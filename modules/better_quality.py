from PIL import Image, ImageFilter
import os
import get_save_folder

def improve_image_quality():
    # Obtener el directorio donde se guardarán los archivos mejorados
    folder = get_save_folder.get_save_folder()
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # Abrir la imagen
            image = Image.open(os.path.join(folder, filename))

            # Convertir a modo RGB
            image = image.convert('RGB')

            # Aplicar filtro para mejorar la calidad
            image = image.filter(ImageFilter.SHARPEN)

            # Guardar la imagen mejorada con el mismo nombre y añadiendo "_m" al final
            improved_filename = os.path.join(folder, filename.split(".")[0] + "_m.jpg")
            image.save(improved_filename)

            # Eliminar la imagen original
            os.remove(os.path.join(folder, filename))
    
improve_image_quality()
