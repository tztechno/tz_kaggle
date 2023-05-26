######################################

import os

# 新しいディレクトリ名を指定
new_folder = "xxx"

# 現在の作業ディレクトリに新しいディレクトリを作成
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
    
######################################

import shutil

directory = 'kaggle/working/yolo_tracking'
shutil.rmtree(directory)    
    
######################################    

rm -r kaggle/working/yolo_tracking

#再帰的にフォルダ内のファイルやサブディレクトリも削除する

######################################

rm -pf kaggle/working/yolo_tracking

######################################
