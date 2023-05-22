import os
import get_save_folder

folder = get_save_folder.get_save_folder()
def enumerate_files(folder=folder, prefix="chesi_"):
    i = 1
    for filename in os.listdir(folder):
        name, ext = os.path.splitext(filename)
        if not filename.startswith(prefix):
            while True:
                new_filename = prefix + str(i) + ext
                if not os.path.exists(os.path.join(folder, new_filename)):
                    break
                i += 1
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))

enumerate_files()