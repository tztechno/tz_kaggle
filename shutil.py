##################################################

import shutil

source_file = 'source.txt'
destination_folder = 'destination_folder/'

shutil.copy(source_file, destination_folder)
ファイルの移動または名前の変更:
shutil.move()を使用してファイルを移動したり、名前を変更したりできます。

##################################################

import shutil

source_file = 'source.txt'
destination_folder = 'new_destination_folder/'
new_name = 'new_name.txt'

shutil.move(source_file, destination_folder + new_name)
ディレクトリの再帰的なコピー:
shutil.copytree()を使用してディレクトリとその中のファイルを再帰的にコピーできます。

##################################################

import shutil

source_folder = 'source_directory/'
destination_folder = 'destination_directory/'

shutil.copytree(source_folder, destination_folder)
ファイルまたはディレクトリの削除:
shutil.rmtree()を使用してファイルまたはディレクトリを削除できます。

##################################################

import shutil

file_or_folder_to_delete = 'file_or_folder_to_delete/'

shutil.rmtree(file_or_folder_to_delete)

##################################################
