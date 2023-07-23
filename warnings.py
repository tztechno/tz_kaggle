import warnings

# 特定の警告を非表示にする
warnings.filterwarnings("ignore", category=UserWarning)  # Dataset has 0 variance
warnings.filterwarnings("ignore", category=FutureWarning)  # shade is now deprecated
