
import multiprocessing as mp
import time

def func(x):
    return x**2

# マルチプロセスでの処理時間を計測
start_time = time.time()
with mp.Pool(processes=4) as pool:
    results = pool.map(func, range(10000000))
end_time = time.time()
mp_time = end_time - start_time
print(f"マルチプロセスでの処理時間: {mp_time:.4f}秒")


# シングルプロセスでの処理時間を計測
start_time = time.time()
results = [func(i) for i in range(10000000)]
end_time = time.time()
sp_time = end_time - start_time
print(f"シングルプロセスでの処理時間: {sp_time:.4f}秒")

# 処理速度の比較
print(f"マルチプロセス処理速度は、シングルプロセス処理速度の{sp_time/mp_time:.2f}倍です")
