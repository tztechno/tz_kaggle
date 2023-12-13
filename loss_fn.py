def loss_fn(output, target):
    # Ensure that the tensors have the same shape or are compatible
    if output.shape != target.shape:
        # Perform necessary operations to make them compatible (e.g., reshape)
        target = target.view_as(output)
    return torch.sqrt(nn.MSELoss()(output, target))


def loss_fn(output, target):
    print("Output shape:", output.shape)
    print("Target shape:", target.shape)
    return torch.sqrt(nn.MSELoss()(output, target))


