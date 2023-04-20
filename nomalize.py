
X=np.array(dataX0)
X_mean = np.mean(X)
X_std = np.std(X)
X_norm = (X - X_mean) / X_std
dataX=X_norm

