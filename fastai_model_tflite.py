
#trained learn prepared

!pip install tensorflow onnx
!pip install onnx-tf

#save as onnx
batch_size = 1
input_shape = (3,128,128)
torch.onnx.export(learn.model.eval().cpu(), 
                  torch.randn(batch_size, *input_shape), 
                  "model.onnx", opset_version=11)

#save as　tf
import onnx
import tensorflow as tf
from onnx_tf.backend import prepare
onnx_model = onnx.load('model.onnx')
tf_graph = prepare(onnx_model)
tf_graph.export_graph('tf_models')

#save as　tflite
converter = tf.lite.TFLiteConverter.from_saved_model('tf_models')
tflite_model = converter.convert()
open("model.tflite", "wb").write(tflite_model)

