------------------------------------------

import gc
del xxx
gc.collect()

------------------------------------------

import psutil
import os
import time

def get_memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 ** 3)  # Convert bytes to GB
  
while True:
    print(f"Current memory usage: {get_memory_usage():.2f} GB")

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

------------------------------------------
