class ConvBNReLU(nn.Module):
    def __init__(
            self,
            in_channels,
            out_channels,
            kernel_size,
            stride,
            groups=1):
        super(ConvBNReLU, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, stride=stride,
                              padding=1, groups=groups, bias=False)
        self.norm = nn.BatchNorm2d(out_channels, eps=NORM_EPS)
        self.act = nn.ReLU(inplace=True)

    def forward(self, x):
        x = self.conv(x)
        x = self.norm(x)
        x = self.act(x)
        return x
      
      
'''   

  This function defines a module that sequentially applies the Convolution, Batch Normalization, 
  and ReLU (Rectified Linear Unit) activation functions. 
  
  This module is called the Conv-BN-ReLU block and is mainly used in deep neural networks 
  following convolution operations.

  in_channels : number of input channels
  out_channels : number of output channels
  kernel_size : convolution kernel size
  stride : number of strides
  groups : number of groups (default 1)

'''
