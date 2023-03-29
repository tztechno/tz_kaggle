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
learn = cnn_learner(dls, 'resnet26', pretrained=False) #新しいデータはinput,学習はまだ
learn.model.load_state_dict(model) #モデル標準形にこれまでの学習結果を足す
learn.fine_tune(3,0.01)  
torch.save(learn.state_dict(), 'model.pt')

################################### 
