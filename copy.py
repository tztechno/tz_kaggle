######################

cp /path/to/source/file.txt /path/to/destination/directory/

######################

import shutil

shutil.copy(source_file, destination_file)

######################

import shutil

def copy_images_to_folder(paths, destination_folder):
    for path in paths:
        shutil.copy2(path, destination_folder)
        print(f"コピーが完了しました: {path}")
        
image_paths = ['/path/to/image1.jpg', '/path/to/image2.jpg', '/path/to/image3.jpg']
destination_folder = '/path/to/destination_folder'

copy_images_to_folder(image_paths, destination_folder)

######################
