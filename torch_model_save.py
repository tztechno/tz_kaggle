
# save CNNmodel
torch.save(model.state_dict(), 'CNNmodel.pt')   #success

# load CNNmodel
new_model = ConvolutionalNetwork()
new_model.load_state_dict(torch.load('CNNmodel.pt'))
