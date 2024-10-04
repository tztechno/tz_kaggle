
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from collections import Counter

# データセットの作成 (不均衡データ)
X, y = make_classification(n_samples=1000, n_features=20, n_classes=3, 
                           n_clusters_per_class=1, weights=[0.05, 0.15, 0.8], random_state=42)

# 元のクラス分布を確認
print(f"Original class distribution: {Counter(y)}")

# トレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# SMOTEの適用
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# 新しいクラス分布を確認
print(f"Resampled class distribution: {Counter(y_resampled)}")
