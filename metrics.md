When evaluating the performance of a machine learning model, comparing the actual target values (`val_y`) with the predicted values (`val_pred`) is essential. Here are the key metrics used for regression and classification tasks:

---

### **1. Regression Metrics (Continuous Output)**
If your model predicts continuous values (e.g., house prices, temperature), use:

1. **Mean Absolute Error (MAE)**  
   - Average absolute difference between `val_y` and `val_pred`.  
   - Formula:  
     \[
     MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
     \]

2. **Mean Squared Error (MSE)**  
   - Average squared difference between `val_y` and `val_pred`.  
   - Penalizes larger errors more heavily.  
   - Formula:  
     \[
     MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
     \]

3. **Root Mean Squared Error (RMSE)**  
   - Square root of MSE (in same units as `val_y`).  
   - Formula:  
     \[
     RMSE = \sqrt{MSE}
     \]

4. **R² (R-Squared)**  
   - Proportion of variance in `val_y` explained by the model.  
   - Range: [0, 1] (higher is better).  
   - Formula:  
     \[
     R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
     \]

5. **Mean Absolute Percentage Error (MAPE)**  
   - Percentage error relative to `val_y`.  
   - Formula:  
     \[
     MAPE = \frac{100\%}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right|
     \]

---

### **2. Classification Metrics (Categorical Output)**
If your model predicts classes (e.g., spam/not spam), use:

1. **Accuracy**  
   - Fraction of correct predictions.  
   - Formula:  
     \[
     Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
     \]

2. **Precision**  
   - Proportion of true positives among predicted positives.  
   - Formula:  
     \[
     Precision = \frac{TP}{TP + FP}
     \]

3. **Recall (Sensitivity)**  
   - Proportion of true positives captured by the model.  
   - Formula:  
     \[
     Recall = \frac{TP}{TP + FN}
     \]

4. **F1-Score**  
   - Harmonic mean of precision and recall.  
   - Formula:  
     \[
     F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
     \]

5. **Confusion Matrix**  
   - Table showing `TP`, `TN`, `FP`, `FN` counts.

6. **ROC-AUC**  
   - Area under the Receiver Operating Characteristic curve.  
   - Measures model’s ability to distinguish classes (range: 0.5–1.0).

---

### **How to Implement in Python**
#### Regression Example:
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(val_y, val_pred)
mse = mean_squared_error(val_y, val_pred)
rmse = mean_squared_error(val_y, val_pred, squared=False)
r2 = r2_score(val_y, val_pred)

print(f"MAE: {mae:.2f}, MSE: {mse:.2f}, RMSE: {rmse:.2f}, R²: {r2:.2f}")
```

#### Classification Example:
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

accuracy = accuracy_score(val_y, val_pred)
precision = precision_score(val_y, val_pred)  # Use average='macro' for multiclass
recall = recall_score(val_y, val_pred)
f1 = f1_score(val_y, val_pred)
cm = confusion_matrix(val_y, val_pred)

print(f"Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F1: {f1:.2f}")
print("Confusion Matrix:\n", cm)
```

---

### **Key Considerations**
- For **imbalanced datasets**, use precision/recall/F1 instead of accuracy.  
- For **probabilistic predictions**, use log loss or ROC-AUC.  
- Always visualize predictions (`val_y` vs `val_pred` scatter plot for regression, ROC curve for classification).

Let me know if you need help interpreting specific metrics!
