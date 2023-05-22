import time
import moviepy.editor as mp
import os
import get_save_folder
from verify_parameters import params

def remove_sound(filename, i, output_folder):
    video = mp.VideoFileClip(filename)
    new_filename = os.path.join(output_folder, "followchesi_" + str(i) + ".mp4")
    video_without_sound = video.without_audio()
    video_without_sound.write_videofile(new_filename)
    video.close()
    return filename

def finish_remove():
    folder = get_save_folder.get_save_folder()
    output_folder = folder
    files_to_remove = []
    for i, filename in enumerate(os.listdir(folder)):
        if filename.startswith("chesi_") and filename.endswith(".mp4"):
            file_to_remove = remove_sound(os.path.join(folder, filename), i + 1, output_folder)
            files_to_remove.append(file_to_remove)
    for file in files_to_remove:
        os.remove(file)
    time.sleep(25)

finish_remove()
