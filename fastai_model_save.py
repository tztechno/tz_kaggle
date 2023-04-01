################################### 
### first time

from fastai.vision.learner import vision_learner

learn = vision_learner(dls, 'resnet26', metrics=error_rate, path='.').to_fp16()
learn.lr_find(suggest_funcs=(valley, slide))

learn.fine_tune(3,0.01)  
torch.save(learn.state_dict(), 'model.pt')
#not save architechture

################################### 
### second time and after

from fastai.vision.learner import vision_learner

model_path = '/kaggle/input/asl-slice-images-fk0-first-fastai2/model.pt'
model = torch.load(model_path, map_location=torch.device('cpu'))
learn = vision_learner(dls, 'resnet26', pretrained=False)   #アーキテクチャー+新しいデータinput
learn.model.load_state_dict(model)   #アーキテクチャーににトレーニング結果を反映
learn.lr_find(suggest_funcs=(valley, slide))

learn.fine_tune(3,0.01)  
torch.save(learn.state_dict(), 'model.pt')

################################### 

learn.save('model')
#save architechture
learn2 = load_learner('models/model.pth',dls=dls)

################################### 

learn.export('model.pkl')
#save architechture
learn3 = load_learner('model.pkl',dls=dls)

################################### 
# onnxで保存する場合
batch_size = 1
input_shape = (3,128,128)
torch.onnx.export(learn.model.eval().cpu(), torch.randn(batch_size, *input_shape), "model.onnx", opset_version=11)
#save architechture

################################### 

# onnxをロードする場合
import numpy as np
import onnxruntime as ort

learn = vision_learner(dls, 'resnet26', metrics=error_rate, path='.', pretrained=False)
ort_session = ort.InferenceSession(model_path)

input_name = ort_session.get_inputs()[0].name
output_names = [output.name for output in ort_session.get_outputs()]
ort_state_dict = {}
outputs = ort_session.run(output_names, {input_name: input_tensor})
for i, name in enumerate(output_names):
    ort_state_dict[name] = outputs[i]
    
learn.model.load_state_dict(ort_state_dict)
learn.lr_find(suggest_funcs=(valley, slide))

################################### 

'''
Describes the model save format.

ONNX format
In an open source format called Open Neural Network Exchange (ONNX),
A file format for exchanging and reusing models learned in various frameworks.
The ONNX format supports a number of major frameworks including Caffe2, PyTorch, TensorFlow, Keras, CNTK.

Pickle format
A library used for serializing Python objects.
You can easily save your model because the file size is small and you can save Python objects.

PyTorch format
A file format specially designed for PyTorch with the extension ".pt".
It contains all model parameters, architecture and optimization information and is only available within the PyTorch framework.

The ONNX format is suitable for using models across frameworks,
Pickle format is suitable for storing Python objects.
The PyTorch format is only available in the PyTorch framework, but it's easiest to save and load models within PyTorch.


モデル保存形式について

ONNX形式
Open Neural Network Exchange(ONNX)と呼ばれるオープンソース形式で、
様々なフレームワークで学習したモデルを交換・再利用できるようにするためのファイル形式です。
ONNX形式は、Caffe2、PyTorch、TensorFlow、Keras、CNTKなど、多数の主要なフレームワークをサポートしています。

Pickle形式
Pythonオブジェクトの直列化に使われるライブラリーです。
ファイルサイズが小さく、Pythonのオブジェクトを保存できるので、簡単にモデルを保存できます。

PyTorch形式
PyTorchのために特別に設計されたファイル形式で、拡張子は".pt"です。
モデルのパラメーター、アーキテクチャ、最適化の情報をすべて含んでおり、PyTorchフレームワーク内でのみ利用可能です。

ONNX形式は、フレームワークをまたいでのモデルの利用に適しており、
Pickle形式はPythonオブジェクトの保存に適しています。
PyTorch形式はPyTorchフレームワークでのみ利用可能ですが、PyTorch内でのモデルの保存と読み込みが最も簡単です。

'''



