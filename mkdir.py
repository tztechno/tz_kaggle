
######################################

def mkdir_if_not_exist(folder_path, overwrite=False):
    if os.path.exists(folder_path):
        if overwrite:
            shutil.rmtree(folder_path)
            os.makedirs(folder_path)
    else:
        os.makedirs(folder_path)


def rmdir_if_exist(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)

######################################

os.makedirs('datasets', exist_ok=True)

######################################

import os

new_folder = "xxx"

if not os.path.exists(new_folder):
    os.makedirs(new_folder)
    
######################################

import shutil

directory = 'kaggle/working/yolo_tracking'
shutil.rmtree(directory)    
    
######################################    

rm -r kaggle/working/yolo_tracking

######################################

rm -pf kaggle/working/yolo_tracking

######################################
