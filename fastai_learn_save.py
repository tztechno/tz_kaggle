################################### first time

learn = vision_learner(dls, 'resnet26', metrics=error_rate, path='.').to_fp16()

learn.lr_find(suggest_funcs=(valley, slide))

learn.fine_tune(3,0.01)  ### ここで学習

learn.save('my_model')   ### 保存してみる

################################### 繰り返し学習

learn = load_learner('my_model')

dls_new = # 新しいデータを読み込むためのDataLoadersを定義する

learn.dls = dls_new

learn.fine_tune(3, 0.01)  ### さらに詰め込み学習

#################################### 分散学習

from fastai.learner import load_learner
from fastai.ensemble import *

learn.export('model1.pkl')

model1 = load_learner('model1.pkl')
model2 = load_learner('model2.pkl')
learners = [model1, model2]

ensemble_model = ensemble(learners)
ensemble_model.predict('test.jpg')

