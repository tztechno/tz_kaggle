import magic

def get_file_type(file_name):
    mime = magic.Magic()
    file_type = mime.from_file(file_name)
    return file_type
