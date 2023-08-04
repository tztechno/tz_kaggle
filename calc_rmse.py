###########################

import numpy as np

# 真の値と予測値のデータセット
true = np.array([1, 2, 3, 4, 5])
pred = np.array([1.2, 1.8, 2.9, 3.7, 4.9])

# 誤差の計算
errors = true - pred

# RMSEの計算
rmse = np.sqrt(np.mean(errors ** 2))

print("RMSE:", rmse)

###########################

import numpy as np

# Step 1: Import the necessary libraries (NumPy is used for array operations)

def calculate_rmse(actual_values, predicted_values):
    # Step 2: Prepare actual and predicted values
    actual_values = np.array(actual_values)
    predicted_values = np.array(predicted_values)
    
    # Step 3: Compute squared differences
    squared_diff = (predicted_values - actual_values) ** 2
    
    # Step 4: Calculate mean of squared differences
    mean_squared_diff = squared_diff.mean()
    
    # Step 5: Take the square root to get RMSE
    rmse = np.sqrt(mean_squared_diff)
    
    return rmse

# Example usage:
actual_values = [1, 2, 3, 4, 5]
predicted_values = [1.5, 2.2, 2.8, 4.1, 5.3]

rmse_result = calculate_rmse(actual_values, predicted_values)
print("RMSE:", rmse_result)

###########################
