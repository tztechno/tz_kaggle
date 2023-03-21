# model for mdical layers' image
import torch.nn as nn

class Conv3dModel(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size):
        super(Conv3dModel, self).__init__()
        self.conv = nn.Conv3d(in_channels, out_channels, kernel_size)

    def forward(self, x):
        x = self.conv(x)
        return x

# モデルのインスタンス化
model = Conv3dModel(in_channels=3, out_channels=16, kernel_size=3)

# 入力データのテンソルのサイズ(batch_size, in_channels, depth, height, width)
input_tensor = torch.randn(1, 3, 64, 64, 64)

# 畳み込み演算
output_tensor = model(input_tensor)

# 出力データのテンソルのサイズ(batch_size, out_channels, out_depth, out_height, out_width)
print(output_tensor.shape)




# model for movie
import torch.nn as nn

class Conv3dModel(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size):
        super(Conv3dModel, self).__init__()
        self.conv = nn.Conv3d(in_channels, out_channels, kernel_size)

    def forward(self, x):
        x = self.conv(x)
        return x

# モデルのインスタンス化
model = Conv3dModel(in_channels=3, out_channels=16, kernel_size=(3, 3, 3))

# 入力データのテンソルのサイズ(batch_size, in_channels, depth, height, width)
input_tensor = torch.randn(1, 3, 16, 64, 64)

# 畳み込み演算
output_tensor = model(input_tensor)

# 出力データのテンソルのサイズ(batch_size, out_channels, out_depth, out_height, out_width)
print(output_tensor.shape)




# other sample
class Model1(nn.Module):
    def __init__(self, input_shape):
        nn.Module.__init__(self)
        
        self.input_shape = input_shape
        
        self.conv = nn.ModuleList(
            [nn.BatchNorm3d(self.input_shape[0]),
             nn.Conv3d(self.input_shape[0], 64, 3, padding=1), 
             nn.ReLU(), 
             nn.MaxPool3d(2),
             nn.Dropout3d(),
                
             nn.Conv3d(64, 128, 3, padding=1), 
             nn.ReLU(), 
             nn.MaxPool3d(2), 
             nn.Dropout3d(),
                
             nn.Conv3d(128, 256, 3, padding=1), 
             nn.ReLU(), 
             nn.MaxPool3d(2),
             nn.Dropout3d()])
        
        #conv_shape = _output_shape(self.input_shape[1:], self.conv)
        conv_shape = self._infer_shape()
        
        self.fc = nn.ModuleList(
            [nn.Linear(int(conv_shape.prod()), 1024), 
             nn.ReLU(),
             nn.Dropout3d(),
             
             nn.Linear(1024, 1)])
        
        map(_init_fun, self.conv)
        map(_init_fun, self.fc)
        
    def _infer_shape(self):
        x = torch.randn(tuple([1] + map(int, self.input_shape)))
        logging.info('Inferring shape for convolutional part...')
        logging.info(x.shape)
        
        for l in self.conv:
            x = l(x);
            logging.info("==== " + str(l) + " ====")
            logging.info(x.shape)
        
        return torch.tensor(x.shape)
    
    def forward(self, x):
        for l in self.conv:
            x = l(x)
        x = x.view(x.size()[0], -1)
        for l in self.fc:
            x = l(x)
        x = torch.sigmoid(x)
        return x   
    
    
