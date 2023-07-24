from sklearn.decomposition import PCA

# PCAの実行
pca = PCA(n_components=32)
data_reduced = pca.fit_transform(data_array)
