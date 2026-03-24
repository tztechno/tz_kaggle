import psutil
import time
import threading
import numpy as np

class SimpleResourceLogger:
    def __init__(self, interval=2.0):
        self.interval = interval
        self.stop_flag = False
        self.start_time = time.time()
        self.cpu_history = []
        self.mem_history = []
        self.thread = threading.Thread(target=self._log_loop, daemon=True)

    def _log_loop(self):
        # Header for the real-time log
        print(f"{'Elapsed(s)':>10} | {'CPU(%)':>8} | {'Mem(%)':>8}")
        print("-" * 34)
        psutil.cpu_percent(None) # Initial call to calibrate
        
        while not self.stop_flag:
            cpu = psutil.cpu_percent(None)
            mem = psutil.virtual_memory().percent
            elapsed = time.time() - self.start_time
            
            self.cpu_history.append(cpu)
            self.mem_history.append(mem)
            
            print(f"{elapsed:10.1f} | {cpu:8.1f} | {mem:8.1f}")
            time.sleep(self.interval)

    def start(self):
        self.thread.start()

    def stop(self):
        self.stop_flag = True
        self.thread.join(timeout=1)
        total_time = time.time() - self.start_time
        
        # --- Final Summary (English) ---
        print("-" * 34)
        if self.cpu_history:
            max_cpu = max(self.cpu_history)
            avg_cpu = sum(self.cpu_history) / len(self.cpu_history)
            max_mem = max(self.mem_history)
            
            print(f"📊 [CELL PERFORMANCE REPORT]")
            print(f"⏱️  Duration:  {total_time:.2f} s")
            print(f"🔥 CPU Peak:  {max_cpu:5.1f} %  (Avg: {avg_cpu:.1f} %)")
            print(f"💾 Mem Peak:  {max_mem:5.1f} %")
        print("-" * 34 + "\n")

# To use in a cell:
# logger = SimpleResourceLogger(interval=2.0)
# logger.start()

logger = SimpleResourceLogger(interval=2.0)

logger.start()

for i in range(5):
    _ = np.linalg.eig(np.random.rand(2000, 2000))
    time.sleep(1)

logger.stop()
