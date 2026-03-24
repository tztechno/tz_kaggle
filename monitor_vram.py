import time
import threading
import subprocess
import torch

# Global dictionary to track peak VRAM consumption
peak_stats = {}

def logger_gpu_memory(interval=10):
    """Monitors GPU memory usage and records peak values in the background."""
    global peak_stats
    while True:
        try:
            # Query memory for all GPUs via nvidia-smi
            result = subprocess.check_output(
                ["nvidia-smi", "--query-gpu=index,memory.used,memory.total", 
                 "--format=csv,nounits,noheader"],
                encoding='utf-8'
            ).strip()
            
            lines = result.split('\n')
            log_time = time.strftime('%H:%M:%S')
            current_log_parts = []
            
            for line in lines:
                idx, used, total = [x.strip() for x in line.split(',')]
                used_int = int(used)
                
                # Update peak usage tracking
                if idx not in peak_stats or used_int > peak_stats[idx]['peak']:
                    peak_stats[idx] = {'peak': used_int, 'total': total}
                
                current_log_parts.append(f"GPU{idx}: {used}/{total}MB")
            
            # Real-time monitoring print
            print(f"[GPU Log] {log_time} | {' | '.join(current_log_parts)}")
            
        except Exception as e:
            print(f"[GPU Log] Error: {e}")
            break
        time.sleep(interval)

# Start background monitoring thread
monitor_thread = threading.Thread(target=logger_gpu_memory, args=(5,), daemon=True)
monitor_thread.start()

print("--- Starting VRAM Workload ---")

def allocate_vram(device_id, gb_size):
    """Allocates a dummy tensor to consume VRAM."""
    device = f"cuda:{device_id}"
    # Roughly 250 million float32 elements = 1GB
    n_elements = int(gb_size * 250 * 10**6) 
    print(f"Allocating ~{gb_size}GB on {device}...")
    return torch.ones((n_elements,), device=device)

try:
    # Simulated workload
    dummy_0 = allocate_vram(0, 8)
    time.sleep(7) 
    
    dummy_1 = allocate_vram(1, 12)
    time.sleep(7) 
    
    print("--- Task complete. Releasing memory. ---")
    del dummy_0, dummy_1
    torch.cuda.empty_cache()
    time.sleep(2) # Brief pause to ensure the final log state is captured

except RuntimeError as e:
    print(f"\n[!] Out of Memory (OOM) Caught: {e}")

# --- Final Peak Summary Display ---
print("\n" + "="*40)
print("📊 FINAL PEAK VRAM USAGE SUMMARY")
print("="*40)
if not peak_stats:
    print("No GPU data recorded.")
else:
    for gpu_id, stats in sorted(peak_stats.items()):
        print(f"GPU {gpu_id}: Peak {stats['peak']} MB / Total {stats['total']} MB")
print("="*40)
