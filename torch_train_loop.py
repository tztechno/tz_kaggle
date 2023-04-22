#######################################################   
#used in MyCNN, AlexNet
#not available in MobileNet,ResNet,EfficientNet,InceptionNet

import time
start_time=time.time()
train_losses=[]
test_losses=[]
train_correct=[]
test_correct=[]

for i in range(epochs):
    trn_corr=0
    tst_corr=0
    for b, (X_train,y_train) in enumerate(train_loader):
        b+=1

        y_pred=model(X_train)
        loss=criterion(y_pred,y_train)       
        #Update parameters
        predicted=torch.max(y_pred.data,1)[1]
        batch_corr=(predicted==y_train).sum()
        trn_corr+= batch_corr

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if b%200==0:
            print(f'epoch: {i:2}  batch: {b:4} [{10*b:6}/8000]  loss: {loss.item():10.8f}  \
accuracy: {trn_corr.item()*100/(10*b):7.3f}%')

    loss=loss.detach().numpy()
    train_losses.append(loss)
    train_correct.append(trn_corr)

    with torch.no_grad():
        for b, (X_test,y_test) in enumerate(test_loader):
            b+=1

            y_val=model(X_test)
            predicted=torch.max(y_val.data,1)[1]
            btach_corr=(predicted==y_test).sum()
            tst_corr+=btach_corr

    loss=criterion(y_val,y_test)
    loss=loss.detach().numpy()
    test_losses.append(loss)
    test_correct.append(tst_corr)

print(f'\nDuration: {time.time() - start_time:.0f} seconds')   

 
#######################################################   
###used in InceptionNet

max_acc=0
train_acc = []
val_acc = []

for epoch in range(n_epochs):
    train_loss = 0
    val_loss = 0
    acc = 0.0
    print("Training....")
    model.train()
    
    for batch_num,(batch,labels) in enumerate(train_loader):
        inp,target = batch.to(device),labels.to(device)
        optimizer.zero_grad()
        output = model.forward(inp)
        
        op = F.softmax(output,dim=1)
        
        final_op = torch.argmax(op,dim=1)
        
        acc += torch.sum(final_op==target).item()/len(target)
        loss = criterion(output,target)
        
        loss.backward()
        optim.step()
        
        train_loss+=(loss.item()/len(batch))
        if batch_num%50 ==0 and batch_num!=0:
            print("TARGET: ",target)
            print("OUTPUT: ",final_op)
            print("Accuracy after ",batch_num,"steps: ",acc/batch_num)
        
    
    acc = acc/len(train_loader)
    train_acc.append(acc)
    print("Epoch: ",epoch,"Loss: ",train_loss," Accuracy: ",acc)
    
    eval_acc = 0
         
    # set model to evaluation mode
    
    # Turn off gradients for validation, saves memory and computations
    with torch.no_grad():
        model.eval()
        print("Validating.....")

        for batch in valid_loader:
            inp,target = batch[0].to(device),batch[1].to(device)
            op = F.softmax(model.forward(inp))
            final_op = torch.argmax(op,dim=1)

            eval_acc += np.sum(final_op.detach().cpu().numpy()==target.detach().cpu().numpy())/len(target)
        
    print("Validation accuracy: ",eval_acc/len(valid_loader))
    val_acc.append(eval_acc/len(valid_loader))
    if eval_acc>max_acc:
        max_acc = eval_acc
        torch.save(model,"model.pt")
    #print("FOP",final_op)
    #print("TARGET",target)
    
#######################################################    
