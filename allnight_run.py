 Local PC allnight 実行方法: papermill (Notebook専用ツール、推奨!)

# 環境をactivate
conda activate kaggle_local_env

# papermillで実行 + caffeinate
caffeinate -i nohup papermill \
  input.ipynb \
  output_$(date +%Y%m%d_%H%M%S).ipynb \
  > papermill.log 2>&1 &

terminalでenvを選び、ノート実行開始時にも同じenvを選ぶ、というプロセスがあった

