def collate_fn(batch):
    images, labels = zip(*batch)
    images = torch.stack([image for image in images], dim=0)
    labels = torch.stack([label for label in labels], dim=0)
    images = A.Resize(0.1, 0.1)(images=images)
    return images, labels
