!pip install tabula-py

import tabula
import pandas as pd

# PDFファイルを読み込んで表を抽出する
df = tabula.read_pdf("example.pdf", pages='all')

# Pandas DataFrameに変換する
df = pd.DataFrame(df[0])

# データフレームの表示
print(df)
