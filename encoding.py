###################################################

byte_sequence = b'...'  # Your byte sequence here
cleaned_sequence = b''.join([x if 32 <= x < 127 else b'?' for x in byte_sequence])
decoded_string = cleaned_sequence.decode('utf-8')

###################################################

import pandas as pd
import chardet

# Read the file in binary mode and detect the encoding
with open('file.csv', 'rb') as f:
    result = chardet.detect(f.read())

# Use the detected encoding to read the CSV file
df = pd.read_csv('file.csv', encoding=result['encoding'])

###################################################
