def predict(data_loader, model):
        
    model.to('cpu')
    model.eval()    
    predictions = []
    for en in range(len(ds_test)):
        print(en)
        images = torch.from_numpy(ds_test[en])
        print(images.shape)
        with torch.no_grad():
            outputs = model(images).sigmoid().detach().cpu().numpy()
            print(outputs.shape)
        predictions.append(outputs)
               
    return predictions
  
