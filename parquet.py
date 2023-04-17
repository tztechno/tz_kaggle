import pyarrow as pa
import pyarrow.parquet as pq

path='d3/'+str(pid)+'_'+str(sid)+'.parquet'
tensor = pa.Tensor.from_numpy(A[1:])
pq.write_tensor(tensor,path)   
