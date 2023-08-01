from sklego.linear_model import LADRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Assuming you have your data in X (input features) and y (target variable)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the LAD regression model
lad_model = LADRegression()
lad_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = lad_model.predict(X_test)

# Evaluate the model using Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)
