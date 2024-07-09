#インスタンス一覧

import sys
import gc

for obj in gc.get_objects():
    if isinstance(obj, pd.DataFrame):
        memory_usage = obj.memory_usage().sum() / 1e6
        if memory_usage > 0:
            print(f"DataFrame: {obj.shape}, Memory usage: {memory_usage:.2f} MB")
    elif isinstance(obj, np.ndarray):
        memory_usage = obj.nbytes / 1e6
        if memory_usage > 0:
            print(f"NumPy array: {obj.shape}, Memory usage: {memory_usage:.2f} MB")

---------------------------------------------

!cat /proc/cpuinfo
!cat /proc/meminfo
!df -h

---------------------------------------------
