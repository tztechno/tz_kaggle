
# torch.nn.Conv3d(in_channels, out_channels, kernel_size, stride=1, padding=0, 
# dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)

# With square kernels and equal stride
m = nn.Conv3d(16, 33, 3, stride=2)
# non-square kernels and unequal stride and with padding
m = nn.Conv3d(16, 33, (3, 5, 2), stride=(2, 1, 1), padding=(4, 2, 0))
input = torch.randn(20, 16, 10, 50, 100)
output = m(input)



###########################################################################

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



###########################################################################

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



###########################################################################

# other sample
class Conv3DNet(nn.Module):
    """
    The C3D network.
    """
    def __init__(self, pretrained=False):
        super(Conv3DNet, self).__init__()

        self.conv1 = nn.Conv3d(3, 64, kernel_size=(3, 3, 3), padding=(1, 1, 1))
        self.pool1 = nn.MaxPool3d(kernel_size=(1, 2, 2), stride=(1, 2, 2))
        self.batch1 = nn.BatchNorm3d(64)

        self.conv2 = nn.Conv3d(64, 128, kernel_size=(3, 3, 3), padding=(1, 1, 1))
        self.pool2 = nn.MaxPool3d(kernel_size=(1, 2, 2), stride=(1, 2, 2))
        self.batch2 = nn.BatchNorm3d(128)

        self.conv3 = nn.Conv3d(128, 256, kernel_size=(3, 3, 3), padding=(1, 1, 1))
        self.pool3 = nn.MaxPool3d(kernel_size=(1, 2, 2), stride=(1, 2, 2))
        self.batch3 = nn.BatchNorm3d(256)

        self.conv4 = nn.Conv3d(256, 512, kernel_size=(3, 3, 3), padding=(1, 1, 1))
        self.pool4 = nn.MaxPool3d(kernel_size=(1, 2, 2), stride=(1, 2, 2))
        self.batch4 = nn.BatchNorm3d(512)

        self.conv5a = nn.Conv3d(512, 256, kernel_size=(3, 3, 3), padding=(1, 1, 1))
        self.conv5b = nn.Conv3d(256, 256, kernel_size=(3, 3, 3), padding=(1, 1, 1))
        self.pool5 = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2))
        self.batch5 = nn.BatchNorm3d(256)

        self.conv6a = nn.Conv3d(256, 20, kernel_size=(3, 3, 3), padding=(1, 1, 1))
        self.conv6b = nn.Conv3d(20, 20, kernel_size=(3, 3, 3), padding=(1, 1, 1))
        self.pool6 = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2))
        self.batch6 = nn.BatchNorm3d(20)

        self.relu = nn.ReLU()
        self.flat = Flatten()

    def forward(self, x):

        x = self.relu(self.conv1(x))
        x = self.batch1(self.pool1(x))
        #print(x.shape)

        x = self.relu(self.conv2(x))
        x = self.batch2(self.pool2(x))
        #print(x.shape)

        x = self.relu(self.conv3(x))
        x = self.batch3(self.pool3(x))
        #print(x.shape)

        x = self.relu(self.conv4(x))
        x = self.batch4(self.pool4(x))
        #print(x.shape)

        x = self.relu(self.conv5a(x))
        x = self.relu(self.conv5b(x))
        x = self.batch5(self.pool5(x))
        #print(x.shape)

        x = self.relu(self.conv6a(x))
        x = self.relu(self.conv6b(x))
        x = self.batch6(self.pool6(x))
        #print(x.shape)

        x = self.flat(x) 

        return 


###########################################################################

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        h_dim = [32, 64, 128]
        self.net = nn.Sequential(
            nn.Conv3d(1, h_dim[0], 4, 2, 1), # 128, 128, 50
            nn.BatchNorm3d(h_dim[0]),
            nn.Dropout(0.05),
            nn.MaxPool3d((2,2,2)),  # 64, 64,50
            nn.Conv3d(h_dim[0], h_dim[1], 4, 2, 1), # 32, 32,12
            nn.BatchNorm3d(h_dim[1]),
            nn.Dropout(0.05),
            nn.MaxPool3d((2,2,2)),   # 16, 16,12
            nn.Conv3d(h_dim[1], h_dim[2], 4, 2, 1),  # 8, 8, 3
            nn.BatchNorm3d(h_dim[2]),
            nn.Dropout(0.05),
            nn.MaxPool3d((4,4,1)), # 2, 2, 3
            View((-1, h_dim[-1]*2*2*3)),
            nn.Linear(h_dim[-1]*2*2*3, 128),
            nn.ReLU(True),
            nn.Linear(128, 1))
    
    def forward(self, x):
        #x: [bz, 1, 256, 256, 400]
        x = self.net(x)
        x = torch.sigmoid(x)
        eps = 1e-6
        x = 0.5*eps + (1-eps)*x
        return x
    
    
    
###########################################################################

def get_model(width=128, height=128, depth=64):
    """Build a 3D convolutional neural network model."""

    inputs = keras.Input((width, height, depth, 1))

    x = layers.Conv3D(filters=64, kernel_size=3, activation="relu")(inputs)
    x = layers.MaxPool3D(pool_size=2)(x)
    x = layers.BatchNormalization()(x)

    x = layers.Conv3D(filters=64, kernel_size=3, activation="relu")(x)
    x = layers.MaxPool3D(pool_size=2)(x)
    x = layers.BatchNormalization()(x)

    x = layers.Conv3D(filters=128, kernel_size=3, activation="relu")(x)
    x = layers.MaxPool3D(pool_size=2)(x)
    x = layers.BatchNormalization()(x)

    x = layers.Conv3D(filters=256, kernel_size=3, activation="relu")(x)
    x = layers.MaxPool3D(pool_size=2)(x)
    x = layers.BatchNormalization()(x)

    x = layers.GlobalAveragePooling3D()(x)
    x = layers.Dense(units=512, activation="relu")(x)
    x = layers.Dropout(0.3)(x)

    outputs = layers.Dense(units=1, activation="sigmoid")(x)

    # Define the model.
    model = keras.Model(inputs, outputs, name="3dcnn")
    return model



###########################################################################

model = Sequential()
model.add(Conv3D(64,(3,3,3), input_shape=(16,16,16,3), padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.25))
model.add(MaxPool3D(pool_size=(2, 2, 2)))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

 

###########################################################################   
  
    
