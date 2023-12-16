
####################################################

# save model
torch.save(model.state_dict(), 'model.pt')

# load model
model = MyModel()
model.load_state_dict(torch.load('model.pt'))

####################################################

####Torch save

model=fitted_model

state = {
                        'state_dict': model.state_dict(),
                        'optimizer_dict': optimizer.state_dict(),
                        "bestscore":bestscore
                    }

torch.save(state, "model0.pth")


####Torch load

model = initialized_model

mpath="/kaggle/input/ai-generated-deberta-v3-base-w-ext-split-rep"

pthes = [os.path.join(mpath,s) for s in os.listdir(mpath) if ".pth" in s]

for pth in pthes:        
    state = torch.load(pth)        
    model.load_state_dict(state["state_dict"])
    model.to(device)
    model.eval()    

####################################################
