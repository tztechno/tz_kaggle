##----------------------------------------------------------------------------------

class LightCNNRegressor(LightningModule):
    def __init__(self, input_dim):
        super().__init__()
        self.model = nn.Sequential(
            nn.Unflatten(1, (1, input_dim)),  # (B, C, L) 形式に変換
            nn.Conv1d(1, 16, kernel_size=3, padding=1),  # 32→16に削減
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(16, 32, kernel_size=3, padding=1),  # 64→32に削減
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Flatten(),
            nn.Linear(32 * (input_dim // 4), 10),  # 中間層も削減
            nn.ReLU(),
            nn.Linear(10, 1)
        )

##----------------------------------------------------------------------------------

class CNNRegressor(LightningModule):
    def __init__(self, input_dim, input_channels=1):
        super().__init__()
        self.input_dim = input_dim
        self.input_channels = input_channels
        
        self.model = nn.Sequential(
            # First reshape the input to (batch_size, channels, length)
            nn.Unflatten(1, (input_channels, input_dim)),
            
            # First convolutional block
            nn.Conv1d(input_channels, 32, kernel_size=3, padding=1),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2),
            
            # Second convolutional block
            nn.Conv1d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2),
            
            # Third convolutional block
            nn.Conv1d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2),
            
            # Flatten the output
            nn.Flatten(),
            
            # Calculate the size after convolutions and pooling
            # input_dim -> input_dim/2 -> input_dim/4 -> input_dim/8
            nn.Linear(128 * (input_dim // 8), 50),
            nn.ReLU(),
            nn.Linear(50, 1)
        )
        
    def forward(self, x):
        return self.model(x)
        
    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.mse_loss(y_hat, y.unsqueeze(1))
        self.log("train_loss", loss)
        return loss
        
    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.mse_loss(y_hat, y.unsqueeze(1))
        self.log("val_loss", loss)
        return loss
        
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.001)

##----------------------------------------------------------------------------------
