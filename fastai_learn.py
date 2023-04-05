

learn = vision_learner(dls, arch=resnet50, opt_func=opt_func, loss_func=loss_func, cbs=cbs, metrics=metrics)

learn = vision_learner(dls, 'resnet26d', metrics=error_rate, path='.').to_fp16()

learn = vision_learner(dls, arch, loss_func=disease_loss, metrics=disease_err, n_out=10).to_fp16()

learn = vision_learner(dls, resnet18, metrics=error_rate)









