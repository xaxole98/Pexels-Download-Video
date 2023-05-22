import os
import shutil
import get_save_folder

def save_folder_finish():
    save_folder = get_save_folder.get_save_folder()
    save_folder_finish = os.path.join(os.path.dirname(save_folder), os.path.basename(save_folder) + "_finish")
    
    if os.path.isdir(save_folder_finish): # Verificar si la carpeta de finalización ya existe
        files = os.listdir(save_folder)
        for file in files:
            src_path = os.path.join(save_folder, file)
            dst_path = os.path.join(save_folder_finish, file)
            shutil.move(src_path, dst_path)
    else:
        os.mkdir(save_folder_finish)
        files = os.listdir(save_folder)
        for file in files:
            src_path = os.path.join(save_folder, file)
            dst_path = os.path.join(save_folder_finish, file)
            shutil.move(src_path, dst_path)
            
    return save_folder_finish

save_folder_finish()
