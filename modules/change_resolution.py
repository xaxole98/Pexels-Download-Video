import ffmpeg
import os
from verify_parameters import params
import get_save_folder
from moviepy.video.io.VideoFileClip import VideoFileClip
from PIL import Image

def change_resolution():
    folder = get_save_folder.get_save_folder()
    resolution = params.resolution

    for filename in os.listdir(folder):
        if filename.endswith(".mp4") or filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            filepath = os.path.join(folder, filename)

            # Get file format and new file name
            file_format = filename.split(".")[-1]
            new_filename = filename.split(".")[0] + "_resolution." + file_format
            new_filepath = os.path.join(folder, new_filename)

            # Check if the resolution is already the desired one
            if file_format in ["png", "jpg","jpeg"]:
                with Image.open(filepath) as img:
                    if img.size == (resolution.split(":")[0], resolution.split(":")[1]):
                        continue
            elif file_format == "mp4":
                with VideoFileClip(filepath) as video:
                    if video.size == (resolution.split(":")[0], resolution.split(":")[1]):
                        continue

            if resolution == "16:9":
                frame_width = 1920
                frame_height = 1080
            elif resolution == "9:16":
                frame_width = 1080
                frame_height = 1920
            else:
                return

            try:
                if file_format in ["png", "jpg","jpeg"]:
                    with Image.open(filepath) as img:
                        img = img.resize((frame_width, frame_height))
                        img.save(new_filepath)
                elif file_format == "mp4":
                    os.system(f"ffmpeg -i {filepath} -vf scale={frame_width}:{frame_height} {new_filepath}")
            except Exception as e:
                print(f"An error occurred while processing {filename}: {e}")

            # Delete original file
            os.remove(filepath)

change_resolution()