
///////////////////////
#from onnx

tf_model_path = "tf_MLP"
onnx_asl_module = onnx.load("MLP.onnx")
tf_rep = prepare(onnx_asl_module)
tf_rep.export_graph(tf_model_path)

class TFModel(tf.Module):
    def __init__(self, tf_model_path):
        super().__init__()

        self.feature_gen = FeatureGen()
        self.model = tf.saved_model.load(tf_model_path)
        self.feature_gen.trainable = False
        self.model.trainable = False

    @tf.function(
        input_signature=[
            tf.TensorSpec(shape=[None, 543, 3], dtype=tf.float32, name="inputs")
        ]
    )
    def call(self, input):
        output_tensors = {}
        features = self.feature_gen(tf.cast(input, dtype=tf.float32))

        output_tensors["outputs"] = self.model(**{"input": features})["output"][0, :]

        return output_tensors


mytfmodel = TFModel("./tf_MLP")
tf.saved_model.save(
    mytfmodel, "tf_infer_model", signatures={"serving_default": mytfmodel.call}
)

tf_infer_model_path = "./tf_infer_model"
converter = tf.lite.TFLiteConverter.from_saved_model(tf_infer_model_path)
tflite_model = converter.convert()

tflite_model_path = "model.tflite"

# Save the model
with open(tflite_model_path, "wb") as f:
    f.write(tflite_model)


///////////////////////
#from keras model

converter = tf.lite.TFLiteConverter.from_keras_model(final_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
with open('./model.tflite', 'wb') as f:
    f.write(tflite_model)


///////////////////////
#from keras model
def get_inference_model(model):
    inputs = tf.keras.Input(shape=(ROWS_PER_FRAME,3), name="inputs")
    
    # drop most of the face mesh
    x = tf.gather(inputs, LANDMARK_IDX, axis=1)

    # fill nan
    x = tf.where(tf.math.is_nan(x), tf.zeros_like(x), x)

    # flatten landmark xyz coordinates ()
    x = tf.concat([x[...,i] for i in range(3)], -1)

    x = tf.expand_dims(x,0)
    
    # call trained model
    out = model(x)
    
    # explicitly name the final (identity) layer for the submission format
    out = layers.Activation("linear", name="outputs")(out)
    
    inference_model = tf.keras.Model(inputs=inputs, outputs=out)
    inference_model.compile(loss="sparse_categorical_crossentropy",
                            metrics="accuracy")
    return inference_model

inference_model = get_inference_model(model)

# save the model
converter = tf.lite.TFLiteConverter.from_keras_model(inference_model)
tflite_model = converter.convert()
model_path = "model.tflite"

# submit the model
with open(model_path, 'wb') as f:
    f.write(tflite_model)
!zip submission.zip $model_path

///////////////////////
#from torch
x = torch.randn(2, 5796, requires_grad=True).to("cuda")
# torch_out = torch_model(x)

model = model.to("cuda")

torch.onnx.export(model,               
                  x,                   
                  "MLP.onnx",   
                  export_params=True,  
                  opset_version=10,    
                  do_constant_folding=True, 
                  input_names = ['input'],  
                  output_names = ['output'],
                  dynamic_axes={'input' : {0 : 'batch_size'},   
                                'output' : {0 : 'batch_size'}})

tf_model_path = "tf_MLP"
onnx_asl_module = onnx.load("MLP.onnx")
tf_rep = prepare(onnx_asl_module)
tf_rep.export_graph(tf_model_path)

class TFModel(tf.Module):
    def __init__(self, tf_model_path):
        super().__init__()

        self.feature_gen = FeatureGen()
        self.model = tf.saved_model.load(tf_model_path)
        self.feature_gen.trainable = False
        self.model.trainable = False

    @tf.function(
        input_signature=[
            tf.TensorSpec(shape=[None, 543, 3], dtype=tf.float32, name="inputs")
        ]
    )
    def call(self, input):
        output_tensors = {}
        features = self.feature_gen(tf.cast(input, dtype=tf.float32))

        output_tensors["outputs"] = self.model(**{"input": features})["output"][0, :]

        return output_tensors


mytfmodel = TFModel("./tf_MLP")
tf.saved_model.save(
    mytfmodel, "tf_infer_model", signatures={"serving_default": mytfmodel.call}
)

tf_infer_model_path = "./tf_infer_model"

converter = tf.lite.TFLiteConverter.from_saved_model(tf_infer_model_path)
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
converter.allow_custom_ops = True

tflite_model = converter.convert()

tflite_model_path = "model.tflite"

# Save the model
with open(tflite_model_path, "wb") as f:
    f.write(tflite_model)

///////////////////////
