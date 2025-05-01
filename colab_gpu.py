ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

import subprocess
result = subprocess.run(
    ['nvidia-smi', '--query-gpu=name', '--format=csv,noheader'],
    stdout=subprocess.PIPE, text=True
)
gpu_name = result.stdout.strip()
if "L4" in gpu_name:
    print(f"✅ L4 detected: {gpu_name} → 実験続行")
else:
    print(f"⛔ Not L4 (detected: {gpu_name}) → セル停止")
    import sys; sys.exit(0)

ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


!nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory,memory.used,memory.total --format=csv



ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

