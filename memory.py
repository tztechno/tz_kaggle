------------------------------------------

import gc
del xxx
gc.collect()

------------------------------------------

!pip install psutil

import psutil
import time

def watch_memory(interval=1.0, duration=30.0):
    print(f"{'Time':>6} | {'Memory (MB)':>12}")
    print("-" * 24)
    start_time = time.time()
    while time.time() - start_time < duration:
        mem = psutil.Process().memory_info().rss / 1024**2  # in MB
        elapsed = time.time() - start_time
        print(f"{elapsed:6.1f} | {mem:12.2f}")
        time.sleep(interval)

# 30秒間、1秒ごとに監視
watch_memory(interval=1.0, duration=30.0)

------------------------------------------

!pip install psutil
import os
import psutil
print("psutil imported successfully")
process = psutil.Process(os.getpid())
print(f"Memory usage: {process.memory_info().rss / 1024 ** 2:.2f} MB")

------------------------------------------

import tracemalloc
tracemalloc.start()

def print_memory():
    snapshot = tracemalloc.take_snapshot()
    total_memory = sum(stat.size for stat in snapshot.statistics('lineno')) 
    total_memory_mb = total_memory / 1024**2  
    print(f"{total_memory_mb:.2f} MB")

print_memory()

------------------------------------------

!cat /proc/meminfo | head -n 5  

#MemTotal:       32873372 kB
#MemFree:        30534464 kB
#MemAvailable:   31577840 kB
#Buffers:           71056 kB
#Cached:          1113564 kB

------------------------------------------
