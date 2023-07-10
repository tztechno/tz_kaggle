import seaborn as sns
import matplotlib.pyplot as plt

# サンプルデータの作成
data = [0.5, 0.7, 1.2, 1.5, 2.0, 2.2, 2.5, 2.7, 3.0, 3.5, 3.7, 4.0, 4.2, 4.5, 4.7, 5.0]

# ヒストグラムのプロット
sns.distplot(data)

# グラフの表示
plt.show()
