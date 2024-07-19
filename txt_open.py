
def txt_open(path):
   with open(path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    L = [line.strip() for line in lines]
    return L 
