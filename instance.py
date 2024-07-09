#インスタンス一覧

import sys
import gc

for obj in gc.get_objects():
    if isinstance(obj, pd.DataFrame):
        print(f"DataFrame: {obj.shape}, Memory usage: {obj.memory_usage().sum() / 1e6:.2f} MB")

---------------------------------------------

!cat /proc/cpuinfo
!cat /proc/meminfo
!df -h

---------------------------------------------
