
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
dataXar = scaler.fit_transform(dataX)
dataX2=pd.DataFrame(dataXar)
dataX2.columns=dataX.columns.tolist()
