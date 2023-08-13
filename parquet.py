
#################################################################

import pyarrow as pa
import pyarrow.parquet as pq

path='d3/'+str(pid)+'_'+str(sid)+'.parquet'
tensor = pa.Tensor.from_numpy(A[1:])
pq.write_tensor(tensor,path)   

#################################################################

parquet_file_path = 'your_file.parquet'

# Read the Parquet file into a DataFrame
df = pd.read_parquet(parquet_file_path)

# Now you can work with the DataFrame 'df'
print(df.head())  # Display the first few rows of the DataFrame

#################################################################
