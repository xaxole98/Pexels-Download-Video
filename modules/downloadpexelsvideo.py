import get_save_folder
import os
from verify_parameters import params
import time
import subprocess
import requests

api_keys = params.api_keys
orientation = params.orientation
size = params.size
default_page = params.page
default_per_page = params.per_page
query = params.query 
folder = get_save_folder.get_save_folder()

def get_user_input():
    print("Do you want to set a different page number? (press enter to use default value)")
    user_input = input()
    if user_input:
        page = user_input
    else:
        page = default_page

    print("Do you want to set a different per page number? (press enter to use default value)")
    user_input = input()
    if user_input:
        per_page = user_input
    else:
        per_page = default_per_page
    
    return page, per_page

def get_videos(api_keys, orientation, size, page, per_page, query):
    headers = {
        "Authorization": " ".join(api_keys),
    }
    response = requests.get(f"https://api.pexels.com/videos/search?query={query}&per_page={per_page}&page={page}&orientation={orientation}&size={size}", headers=headers)
    if response.status_code != 200:
        print("API call failed with status code:", response.status_code)
        return
    videos = response.json()["videos"]
    video_count = 0
    for video in videos:
        video_url = video["video_files"][0]["link"]
        video_response = requests.get(video_url)
        with open(os.path.join(folder, str(video["id"]) + ".mp4"), "wb") as f:
            f.write(video_response.content)
        video_count += 1
        if video_count == per_page:
            break
    print("Download complete. Press Enter")
    user_input = input()
    # Ask the user if they want to run id_numeration
    answer = input("Do you want to run better_quality_video? (y/n): ")
    if answer.lower() == "y":
        result = subprocess.run(["python", "modules/better_quality_video.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("better_quality_video completed successfully\n")
        else:
            print("better_quality_video failed with error code:\n", result.returncode)
    else:
        print("better_quality_video skipped\n")
    # Ask the user if they want to run id_numeration
    answer = input("Do you want to run id_numeration? (y/n): ")
    if answer.lower() == "y":
        result = subprocess.run(["python", "modules/id_numeration.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("id_numeration completed successfully\n")
        else:
            print("id_numeration failed with error code:\n", result.returncode)
    else:
        print("id_numeration skipped\n")  
            
    # Ask the user if they want to run change_resolution
    answer = input("Do you want to run change_resolution? (y/n): ")
    if answer.lower() == "y":
        result = subprocess.run(["python", "modules/change_resolution.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("change_resolution completed successfully\n")
        else:
            print("change_resolution failed with error code:\n", result.returncode)
    else:
        print("change_resolution skipped\n")
    # Ask the user if they want to run remove_sound
    answer = input("Do you want to run remove_sound? (y/n): ")
    if answer.lower() == "y":
        result = subprocess.run(["python", "modules/remove_sound.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("remove_sound completed successfully\n")
        else:
            print("remove_sound failed with error code:\n", result.returncode)
    else:
        print("remove_sound skipped\n")
    # Ask the user if they want to run save_folder_finish
    answer = input("Do you want to run save_folder_finish? (y/n): ")
    if answer.lower() == "y":
        result = subprocess.run(["python", "modules/save_folder_finish.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("save_folder_finish completed successfully\n")
        else:
            print("save_folder_finish failed with error code:\n", result.returncode)
    else:
        print("save_folder_finish skipped\n")
          
                
page, per_page = get_user_input()
get_videos(api_keys, orientation, size, page, per_page, query)