################################### 
### first time

learn = vision_learner(dls, 'resnet26', metrics=error_rate, path='.').to_fp16()
learn.lr_find(suggest_funcs=(valley, slide))

learn.fine_tune(3,0.01)  
torch.save(learn.state_dict(), 'model.pt')

################################### 
### second time and after

from fastai.vision.learner import cnn_learner

model_path = '/kaggle/input/asl-slice-images-fk0-first-fastai2/model.pt'
model = torch.load(model_path, map_location=torch.device('cpu'))
learn = cnn_learner(dls, 'resnet26', pretrained=False) #新しいデータinput
learn.model.load_state_dict(model) #baseモデルにトレーニング結果を反映
learn.lr_find(suggest_funcs=(valley, slide))

learn.fine_tune(3,0.01)  
torch.save(learn.state_dict(), 'model.pt')

################################### 

# onnxで保存する場合
batch_size = 1
input_shape = (3,128,128)
torch.onnx.export(learn.model, torch.randn(batch_size, *input_shape), "model.onnx", opset_version=11)

################################### 

# onnxをロードする場合
import numpy as np
import onnxruntime

learn = cnn_learner(dls, 'resnet26', metrics=error_rate, path='.', pretrained=False)
ort_session = onnxruntime.InferenceSession(model_path)
ort_state_dict = {}
for i, name in enumerate(ort_session.get_outputs()):
    ort_state_dict[name.name] = ort_session.get_outputs()[i].detach().cpu().numpy()
learn.model.load_state_dict(ort_state_dict)
learn.lr_find(suggest_funcs=(valley, slide))

################################### 
