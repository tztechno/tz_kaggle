def run_classification_cv(trainX, trainY, testX, n_splits=5, task_type='binary', num_classes=None):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    
    # Initialize predictions arrays
    if task_type == 'binary':
        train_oof = np.zeros(len(trainX))
        test_preds = np.zeros(len(testX))
    elif task_type == 'multiclass':
        train_oof = np.zeros((len(trainX), num_classes))
        test_preds = np.zeros((len(testX), num_classes))
    elif task_type == 'multilabel':
        train_oof = np.zeros((len(trainX), trainY.shape[1]))
        test_preds = np.zeros((len(testX), trainY.shape[1]))
    
    for fold_num, (train_index, val_index) in enumerate(kf.split(trainX)):
        print(f"Fitting fold {fold_num+1}/{n_splits}")
        
        # Split data
        X_train, X_val = trainX[train_index], trainX[val_index]
        y_train, y_val = trainY[train_index], trainY[val_index]
        
        # Convert to tensors
        X_train_tensor = torch.FloatTensor(X_train)
        y_train_tensor = torch.FloatTensor(y_train) if task_type != 'multiclass' else torch.LongTensor(y_train)
        X_val_tensor = torch.FloatTensor(X_val)
        y_val_tensor = torch.FloatTensor(y_val) if task_type != 'multiclass' else torch.LongTensor(y_val)
        
        # Create datasets and dataloaders
        train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
        val_dataset = TensorDataset(X_val_tensor, y_val_tensor)
        
        train_loader = DataLoader(train_dataset, batch_size=256, shuffle=True, num_workers=3)
        val_loader = DataLoader(val_dataset, batch_size=256, num_workers=3)
        
        # Model setup
        output_dim = 1 if task_type == 'binary' else (num_classes if task_type == 'multiclass' else trainY.shape[1])
        model = MLPClassifier(
            input_dim=X_train_tensor.shape[1], 
            output_dim=output_dim,
            task_type=task_type
        )
        
        def fixed_compute_loss_and_metrics(self, batch):
            x, y = batch
            logits = self(x)
            loss = self.loss_fn(logits, y)
            
            with torch.no_grad():  # Add this to prevent gradient tracking during metrics computation
                preds = torch.softmax(logits, dim=1) if self.task_type == 'multiclass' else torch.sigmoid(logits)
                if self.task_type == 'multiclass':
                    preds_class = torch.argmax(preds, dim=1)
                else:
                    preds_class = (preds > 0.5).float()
                
                metrics = {
                    'accuracy': accuracy_score(y.cpu().detach().numpy(), preds_class.cpu().detach().numpy()),
                    'f1_macro': f1_score(y.cpu().detach().numpy(), preds_class.cpu().detach().numpy(), average='macro'),
                }

                if self.task_type == 'multiclass':
                    metrics['log_loss'] = log_loss(
                        y.cpu().detach().numpy(), 
                        preds.cpu().detach().numpy(), 
                        labels=list(range(self.output_dim))
                    )
                else:
                    metrics['log_loss'] = log_loss(
                        y.cpu().detach().numpy(), 
                        preds.cpu().detach().numpy()
                    )
            
            return loss, metrics, logits

        # Trainer setup
        trainer = L.Trainer(
            max_epochs=1000,
            callbacks=[L.callbacks.EarlyStopping(monitor="val_loss", patience=10, mode="min")],
            enable_progress_bar=False,
            enable_model_summary=False
        )
        
        # Training
        trainer.fit(model, train_loader, val_loader)
        
        # Validation predictions
        model.eval()
        with torch.no_grad():
            if task_type == 'binary':
                val_pred = torch.sigmoid(model(X_val_tensor)).squeeze().detach().numpy()
                train_oof[val_index] = val_pred
            elif task_type == 'multiclass':
                val_pred = torch.softmax(model(X_val_tensor), dim=1).detach().numpy()
                train_oof[val_index] = val_pred
            elif task_type == 'multilabel':
                val_pred = torch.sigmoid(model(X_val_tensor)).detach().numpy()
                train_oof[val_index] = val_pred
        
        # Metrics calculation
        with torch.no_grad():
            if task_type == 'binary':
                val_pred_class = (val_pred > 0.5).astype(int)
                print(f"Fold {fold_num+1} - Accuracy: {accuracy_score(y_val, val_pred_class):.4f}, "
                      f"F1: {f1_score(y_val, val_pred_class):.4f}, "
                      f"AUC: {roc_auc_score(y_val, val_pred):.4f}")
            elif task_type == 'multiclass':
                val_pred_class = np.argmax(val_pred, axis=1)
                print(f"Fold {fold_num+1} - Accuracy: {accuracy_score(y_val, val_pred_class):.4f}, "
                      f"F1 Macro: {f1_score(y_val, val_pred_class, average='macro'):.4f}, "
                      f"AUC (OvO): {roc_auc_score(y_val, val_pred, multi_class='ovo'):.4f}")
            elif task_type == 'multilabel':
                val_pred_class = (val_pred > 0.5).astype(int)
                print(f"Fold {fold_num+1} - Accuracy: {accuracy_score(y_val, val_pred_class):.4f}, "
                      f"F1 Macro: {f1_score(y_val, val_pred_class, average='macro'):.4f}")
        
        # Test predictions
        test_tensor = torch.FloatTensor(testX)
        with torch.no_grad():
            if task_type == 'binary':
                test_pred_fold = torch.sigmoid(model(test_tensor)).squeeze().detach().numpy()
                test_preds += test_pred_fold / n_splits
            elif task_type == 'multiclass':
                test_pred_fold = torch.softmax(model(test_tensor), dim=1).detach().numpy()
                test_preds += test_pred_fold / n_splits
            elif task_type == 'multilabel':
                test_pred_fold = torch.sigmoid(model(test_tensor)).detach().numpy()
                test_preds += test_pred_fold / n_splits
        
        # Cleanup
        del X_train_tensor, y_train_tensor, X_val_tensor, y_val_tensor, model
        torch.cuda.empty_cache()
        gc.collect()
    
    # For multiclass, return class predictions for train_oof
    if task_type == 'multiclass':
        train_oof_class = np.argmax(train_oof, axis=1)
        return train_oof_class, test_preds
        
    return train_oof, test_preds
