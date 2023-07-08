
###########################################################################################
import csv


def read_csv_rows(csv_file, start_row, end_row):
    rows = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if start_row <= i + 1 <= end_row:
                rows.append(row)
    return rows


###########################################################################################

import pandas as pd

def read_csv_line_by_line(file_path, encoding):
    data = []
    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            try:
                line_data = pd.read_csv(pd.compat.StringIO(line))
                data.append(line_data)
            except pd.errors.ParserError:
                # Handle the parsing error for the specific line
                print("Parsing error occurred for line:", line)
                # You can choose to skip the line, perform error handling, or take any other action
                # To skip the line, you can use: continue
    return pd.concat(data, ignore_index=True)

file_path = "/kaggle/input/horse-racing-results-2017-2020/Horse Racing Results.CSV"
encoding = 'utf-8'  # Replace with the appropriate encoding

data0 = read_csv_line_by_line(file_path, encoding)
display(data0.info())

###########################################################################################

import chardet

with open("/kaggle/input/horse-racing-results-2017-2020/Horse Racing Results.CSV", 'rb') as f:
    result = chardet.detect(f.read())

data0 = pd.read_csv("/kaggle/input/horse-racing-results-2017-2020/Horse Racing Results.CSV", encoding=result['encoding'])

###########################################################################################
