
# Install FLAML
!pip install flaml

# Import necessary libraries
from flaml import AutoML
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize AutoML instance
automl = AutoML()

# Specify settings for the automl run
settings = {
    "time_budget": 60,  # time budget in seconds
    "metric": 'accuracy',  # evaluation metric
    "task": 'classification',  # task type
}

# Run AutoML
automl.fit(X_train=X_train, y_train=y_train, **settings)

# Predict and evaluate
y_pred = automl.predict(X_test)
accuracy = sum(y_pred == y_test) / len(y_test)
print(f"Accuracy: {accuracy:.4f}")
