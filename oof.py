---------------------------------
oof = final_model.predict(X, num_iteration=final_model.best_iteration_)
np.save('oof.npy',oof)
----------------------------------
X_tensor = torch.tensor(X.values, dtype=torch.float32)

if torch.cuda.is_available():
    X_tensor = X_tensor.cuda()
    model = model.cuda()

model.eval()
with torch.no_grad():
    oof = model(X_tensor).squeeze().cpu().numpy()

np.save('oof.npy', oof)
----------------------------------
