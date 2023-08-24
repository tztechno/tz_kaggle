from imblearn.over_sampling import ADASYN
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=20, n_informative=2,
                           n_redundant=10, n_clusters_per_class=1, weights=[0.1, 0.9],
                           random_state=42)
