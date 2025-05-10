
#################################
from datetime import datetime
import pytz  # タイムゾーン処理用ライブラリ

# 現在時刻をUTCで取得
now_utc = datetime.now(pytz.utc)
print(f"UTC: {now_utc}")


#################################

import time
tstart = time.time()
tend = time.time()
elapsed_time = tend - tstart
print(f"Elapsed time: {elapsed_time} seconds")

#################################

%%time

#################################
