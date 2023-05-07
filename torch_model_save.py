
# save model
torch.save(model.state_dict(), 'model.pt')

# load model
model = MyModel()
model.load_state_dict(torch.load('model.pt'))
