from PIL import Image, ImageFilter
import os
import get_save_folder
import subprocess

def improve_videos_quality():
    folder = get_save_folder.get_save_folder()
    # Obtener lista de archivos de video en la carpeta
    video_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f.endswith('.mp4')]

    for video_file in video_files:
        # Construir los nombres de archivo de entrada y salida
        input_file = os.path.join(folder, video_file)
        output_file = os.path.join(folder, f"{os.path.splitext(video_file)[0]}_m.mp4")

        # Mejorar la calidad del video
        subprocess.call(['ffmpeg', '-i', input_file, '-b:v', '5000k', '-bufsize', '10000k', output_file])

        print(f"Video mejorado y guardado en '{output_file}'")

        # Borrar el archivo original
        os.remove(input_file)
        
improve_videos_quality()