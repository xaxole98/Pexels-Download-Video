from verify_parameters import params
import subprocess

media_type = params.media_type

def download_media():
    if media_type == 'photo':
        subprocess.call(["python", "modules/downloadpexelsphoto.py"])
    elif media_type == 'video':
        subprocess.call(["python", "modules/downloadpexelsvideo.py"])
    else:
        print("Error: media_type - 'photo' or 'video' is only what you can use")
        return

download_media()
