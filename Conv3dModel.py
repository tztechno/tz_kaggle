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
