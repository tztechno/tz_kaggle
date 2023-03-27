
import pyexcel as pe

data = pe.get_array(file_name="example.ods", sheet_name="Sheet1")
print(data)
