########################################

from sklearn.metrics import classification_report

print(classification_report(y_true, y_pred, target_names=class_names, digits=4))

########################################

from collections import Counter

class_counts = Counter(y_true)

sorted_counts = sorted(class_counts.items(), key=lambda x: x[1])
for cls, count in sorted_counts:
    print(f"Class {cls}: {count} samples")

threshold = 8

valid_classes = {cls for cls, count in class_counts.items() if count >= threshold}

filtered_y_true = [y for y in y_true if y in valid_classes]
filtered_y_pred = [y for y, t in zip(y_pred, y_true) if t in valid_classes]  

filtered_labels = sorted(valid_classes)
filtered_class_names = [class_names[i] for i in filtered_labels]

print(classification_report(filtered_y_true, filtered_y_pred, labels=filtered_labels, target_names=filtered_class_names, digits=4))
#print(classification_report(y_true,y_pred,target_names=class_names,digits=4))

########################################

from sklearn.metrics import classification_report

classification_report(y_true, y_pred, 
                      labels=None, target_names=None, 
                      sample_weight=None, digits=2, 
                      output_dict=False, zero_division='warn')
'''
y_true: 真のラベル。shape=(n_samples,)の1次元配列。
y_pred: 予測されたラベル。shape=(n_samples,)の1次元配列。
labels (オプション): 評価するクラスのリスト。省略された場合、すべてのクラスが評価されます。
target_names (オプション): レポートに表示するクラス名のリスト。labelsが省略された場合は必須です。
sample_weight (オプション): 各サンプルの重みを示すshape=(n_samples,)の1次元配列。
digits (オプション): 小数点以下の桁数。
output_dict (オプション): レポートを辞書形式で出力するかどうかを示すブール値。
zero_division (オプション): 0で除算が発生した場合の動作を制御するための文字列または数値。
'''                  
########################################

from sklearn.metrics import classification_report
from keras.utils import to_categorical

val_predictions = model3.predict(val_ds)
val_predicted_labels = np.argmax(val_predictions, axis=1)

val_true_labels = []

# Iterate through the dataset to extract the true labels
for batch in val_ds:
    _, labels = batch  # The first element of the batch is the input data, the second element is the labels
    val_true_labels.extend(labels.numpy())  # Convert the labels tensor to a numpy array and add it to the list

val_true_labels = np.array(val_true_labels)  # Convert to NumPy array if not already
val_true_labels = to_categorical(val_true_labels)  # Convert to multilabel-indicator format

report = classification_report(val_true_labels, val_predicted_labels)

print(report)

########################################
