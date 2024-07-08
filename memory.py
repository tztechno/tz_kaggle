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
