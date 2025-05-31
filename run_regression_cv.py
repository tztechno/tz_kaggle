def run_regression_cv(trainX, trainY, testX, n_splits=5):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    
    # Initialize predictions arrays
    train_oof = np.zeros(len(trainX))
    test_preds = np.zeros(len(testX))
    
    for fold_num, (train_index, val_index) in enumerate(kf.split(trainX)):
        print(f"Fitting fold {fold_num+1}/{n_splits}")
        
        # Split data
        X_train, X_val = trainX[train_index], trainX[val_index]
        y_train, y_val = trainY[train_index], trainY[val_index]
        
        # Convert to tensors
        X_train_tensor = torch.FloatTensor(X_train)
        y_train_tensor = torch.FloatTensor(y_train)
        X_val_tensor = torch.FloatTensor(X_val)
        y_val_tensor = torch.FloatTensor(y_val)
        
        # Create datasets and dataloaders
        train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
        val_dataset = TensorDataset(X_val_tensor, y_val_tensor)
        
        train_loader = DataLoader(train_dataset, batch_size=256, shuffle=True, num_workers=3)
        val_loader = DataLoader(val_dataset, batch_size=256, num_workers=3)
        
        # Model setup
        model = MLPRegressor(
            input_dim=X_train_tensor.shape[1], 
            output_dim=1  # 回帰タスクなので出力は1次元
        )
        
        def fixed_compute_loss_and_metrics(self, batch):
            x, y = batch
            preds = self(x)
            loss = self.loss_fn(preds, y)
            
            with torch.no_grad():  # メトリクス計算時に勾配追跡を防ぐ
                metrics = {
                    'mse': F.mse_loss(preds, y).item(),
                    'mae': F.l1_loss(preds, y).item(),
                    'r2': r2_score(y.cpu().detach().numpy(), preds.cpu().detach().numpy())
                }
            
            return loss, metrics, preds

        # Trainer setup
        trainer = L.Trainer(
            max_epochs=EPOCHS,
            callbacks=[L.callbacks.EarlyStopping(monitor="val_loss", patience=10, mode="min")],
            enable_progress_bar=False,
            enable_model_summary=False
        )
        
        # Training
        trainer.fit(model, train_loader, val_loader)
        
        # Validation predictions
        model.eval()
        with torch.no_grad():
            val_pred = model(X_val_tensor).squeeze().detach().numpy()
            train_oof[val_index] = val_pred
        
        # Metrics calculation
        with torch.no_grad():
            mse = mean_squared_error(y_val, val_pred)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(y_val, val_pred)
            r2 = r2_score(y_val, val_pred)
            
            print(f"Fold {fold_num+1} - MSE: {mse:.4f}, RMSE: {rmse:.4f}, "
                  f"MAE: {mae:.4f}, R2: {r2:.4f}")
        
        # Test predictions
        test_tensor = torch.FloatTensor(testX)
        with torch.no_grad():
            test_pred_fold = model(test_tensor).squeeze().detach().numpy()
            test_preds += test_pred_fold / n_splits
        
        # Cleanup
        del X_train_tensor, y_train_tensor, X_val_tensor, y_val_tensor, model
        torch.cuda.empty_cache()
        gc.collect()
    
    return train_oof, test_preds
