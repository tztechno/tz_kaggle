from sklearn.ensemble import IsolationForest

def remove_outliers(data, contamination=0.05):
    model = IsolationForest(contamination=contamination)
    model.fit(data)
    outliers_mask = model.predict(data) == 1
    filtered_data = data[outliers_mask]
    return filtered_data
