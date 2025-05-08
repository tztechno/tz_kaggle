import time
import os

# 3時間（10800秒）スリープしてからGPU解放（ノートを終了）
time.sleep(10800)
os._exit(0)
