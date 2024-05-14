----------------------------------

import cudf

train = cudf.from_pandas(train) 

----------------------------------

gdf = cudf.read_csv('path/to/csv_file.csv')
print(gdf)

----------------------------------

import pandas as pd

pdf = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': [5, 6, 7, 8]
})
gdf = cudf.DataFrame.from_pandas(pdf)
print(gdf)

----------------------------------

data = {
    'a': [1, 2, 3, 4],
    'b': [5, 6, 7, 8]
}
gdf = cudf.DataFrame(data)
print(gdf)

----------------------------------
