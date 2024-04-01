https://www.kaggle.com/code/stpeteishii/brain-tumor-fit-predict-pytorch-lightning-cnn

################################
[train,fit]

dataset = ImageDataset(path_label)
dataset.setup() 
train_dataloader = dataset.train_dataloader
val_dataloader = dataset.val_dataloader

datamodule = DataModule()
datamodule.setup() 
model = ConvolutionalNetwork()

trainer = pl.Trainer(max_epochs=2)
trainer.fit(model, datamodule)
val_loader = datamodule.val_dataloader()
trainer.test(dataloaders=val_loader)


[test,predict]

tdataset = ImageDataset(tpath_label)
tdataset.setup(stage='Test') 
test_dataloader = tdataset.test_dataloader

datamodule = DataModule()
datamodule.setup(stage='Test') 
test_loader = datamodule.test_dataloader()

trainer.test(dataloaders=test_loader)

################################
