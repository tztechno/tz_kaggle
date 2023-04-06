# dblock.dataloaders

dls = dblock.dataloaders(data)

dls = dblock.dataloaders(path_lr, bs=bs, path=path, item_tfms=Resize(size))

dls =  dblock.dataloaders(train_df, bs=64)

dls = dblock.dataloaders(path)

dls = dblock.dataloaders(data_df, bs=16)

dls = dblock.dataloaders(train_df, num_workers=0)

dls = dblock.dataloaders(data_path, bs=bs, num_workers=0)

dls = dblock.dataloaders(df, path=path, bs=bs, num_workers=num_workers, device=device, **kwargs)

dls = dblock.dataloaders(MARKED, bs=bs, path=DATA)

dls = dblock.dataloaders(
            source=P(config.training.dir).expanduser(),
            item_tfms=item_tfms,
            batch_tfms=batch_tfms
        )


