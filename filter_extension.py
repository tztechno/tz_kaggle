def filter_files_with_extension(directory, extensions):
    file_list = os.listdir(directory)
    filtered_files = [file for file in file_list if not any(file.endswith(ext) for ext in extensions)]
    return filtered_files

extensions_to_exclude = ['jpg!d']

filtered_files = filter_files_with_extension(directory, extensions_to_exclude)
