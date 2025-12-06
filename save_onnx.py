###########################################
import torch

# Lightning training で使ったモデルを eval に
model.eval()

# モデル構造が model.model にある場合はそっちを利用
export_model = model.model if hasattr(model, "model") else model

dummy_input = torch.randn(1, 3, 224, 224)

torch.onnx.export(
    export_model,
    dummy_input,
    "emotion_model.onnx",
    export_params=True,
    opset_version=17,
    do_constant_folding=True,
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={
        'input': {0: 'batch_size'},
        'output': {0: 'batch_size'}
    }
)
###########################################
import tensorflow as tf
import tf2onnx

spec = (tf.TensorSpec(model.input_shape, tf.float32, name="input"),)
output_path = "emotion_model.onnx"
model_proto, _ = tf2onnx.convert.from_keras(model, input_signature=spec, opset=17)
with open(output_path, "wb") as f:
    f.write(model_proto.SerializeToString())

###########################################
