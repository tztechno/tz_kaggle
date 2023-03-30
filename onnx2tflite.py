
import tensorflow as tf
from tensorflow import lite

# ONNX形式のモデルを読み込む
onnx_model = onnx.load("my_model.onnx")

# TensorFlow Lite Converterを初期化する
converter = lite.TFLiteConverter.from_onnx_model(onnx_model)

# 量子化を有効にする（オプション）
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# 入力形式を指定する
input_shape = {"input": [batch_size, *input_shape]}

# 入力/出力テンソル名を指定する
converter.input_arrays = ["input"]
converter.output_arrays = ["output"]

# .tfliteファイルに変換する
tflite_model = converter.convert()
open("my_model.tflite", "wb").write(tflite_model)
