
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
