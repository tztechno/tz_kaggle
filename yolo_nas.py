def collate_fn(batch):
    images, labels = zip(*batch)
    images = torch.stack([image for image in images], dim=0)
    labels = torch.stack([label for label in labels], dim=0)
    images = A.Resize(0.1, 0.1)(images=images)
    return images, labels



# old checkpoint_path=os.path.join(config.CHECKPOINT_DIR, config.EXPERIMENT_NAME, 'average_model.pth')

# now checkpoint_path=os.path.join(trainer.checkpoints_dir_path, "average_model.pth")
