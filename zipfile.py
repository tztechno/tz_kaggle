
################################################################

import zipfile

def create_zip(source_folder, destination_zip):
    with zipfile.ZipFile(destination_zip, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, arcname=os.path.relpath(file_path, source_folder))

def extract_zip(zip_file, destination_folder):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

source_folder = '/kaggle/input/turtle-data-downsized-for-yolo-nas'
destination_zip = '/kaggle/working/folder.zip'
destination_folder = '/kaggle/working/'

create_zip(source_folder, destination_zip)
extract_zip(destination_zip, destination_folder)        
        
################################################################

import zipfile

file_name = 'model.pt'
save_dir = './'

zip_name = 'submission.zip'

with zipfile.ZipFile(zip_name, mode='w') as zipf:
    zipf.write(file_name, arcname=file_name)

################################################################
