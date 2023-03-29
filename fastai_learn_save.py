################################### 
### first time

learn = vision_learner(dls, 'resnet26', metrics=error_rate, path='.').to_fp16()

learn.lr_find(suggest_funcs=(valley, slide))

learn.fine_tune(3,0.01)  

learn.save('my_model')   

################################### 
### second time and after

learn = load_learner('my_model')

learn.dls = dls_new

learn.fine_tune(3, 0.01) 



