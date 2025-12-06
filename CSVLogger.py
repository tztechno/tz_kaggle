if __name__ == '__main__':
    datamodule = DataModule(path_label=path_label)
    datamodule.setup()
    model = ConvolutionalNetwork(num_classes=len(class_names))

    from lightning.pytorch.loggers import CSVLogger
    
    logger = CSVLogger("logs", name="cnn") 
    
    trainer = L.Trainer(
        max_epochs=5,
        logger=logger       
    )
    
    trainer.fit(model, datamodule)
    datamodule.setup(stage='test')
    test_loader = datamodule.test_dataloader()
    trainer.test(dataloaders=test_loader)
