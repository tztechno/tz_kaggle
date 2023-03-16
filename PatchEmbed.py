class PatchEmbed(nn.Module):
    def __init__(self,
                 in_channels,
                 out_channels,
                 stride=1):
        super(PatchEmbed, self).__init__()
        norm_layer = partial(nn.BatchNorm2d, eps=NORM_EPS)
        if stride == 2:
            self.avgpool = nn.AvgPool2d((2, 2), stride=2, ceil_mode=True, count_include_pad=False)
            self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=1, bias=False)
            self.norm = norm_layer(out_channels)
        elif in_channels != out_channels:
            self.avgpool = nn.Identity()
            self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=1, bias=False)
            self.norm = norm_layer(out_channels)
        else:
            self.avgpool = nn.Identity()
            self.conv = nn.Identity()
            self.norm = nn.Identity()

    def forward(self, x):
        return self.norm(self.conv(self.avgpool(x)))
      
   
'''

For example, if the input is an RGB image of size (3, 224, 224) with a patch size of (16, 16) and a stride of 16:

Input: (3, 224, 224)
Patch size: (16, 16)
Stride: 16
Output: (768, 14, 14)

where the first dimension of the output, 768, is equal to the number of patches when the input image is divided 
into 16x16 patches (14x14=196). Each patch is combined in the channel direction to get the output.

'''
  
   
