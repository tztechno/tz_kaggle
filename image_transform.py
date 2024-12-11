
######################################################################
######################################################################
######################################################################
######################################################################


class LogScaleTransform:
    def __call__(self, tensor):
        epsilon = 1e-6
        return torch.log(tensor + epsilon)

class GaussianNoiseTransform:
    def __call__(self, tensor):
        noise = torch.randn(tensor.size()) * 0.1  # 標準偏差0.1のノイズ
        return tensor + noise   

class Cutout:
    def __init__(self, size=50):
        self.size = size

    def __call__(self, img):
        x = torch.randint(0, img.size(1) - self.size, (1,))
        y = torch.randint(0, img.size(2) - self.size, (1,))
        img[:, x:x+self.size, y:y+self.size] = 0
        return img

class MosaicTransform:
    def __call__(self, img):
        img = transforms.Resize((32, 32))(img)  # 低解像度化
        return transforms.Resize((224, 224))(img)  # 元のサイズに戻す

transform=transforms.Compose([
        transforms.RandomRotation(10),      # rotate +/- 10 degrees
        transforms.RandomHorizontalFlip(),  # reverse 50% of images

        LogScaleTransform()           
        GaussianNoiseTransform()
        Cutout(size=50)
        MosaicTransform()   
    
        transforms.RandomRotation(degrees=(-30, 30)) 
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)) 
        transforms.RandomResizedCrop(size=224, scale=(0.8, 1.0))
        transforms.RandomHorizontalFlip(p=0.5) 
        transforms.RandomVerticalFlip(p=0.5)
        transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.1)
        transforms.RandomGrayscale(p=0.2) 
        transforms.RandomCrop(size=(200, 200))
        transforms.RandomPerspective(distortion_scale=0.5, p=0.5)
    
        transforms.Resize(112),             # resize shortest side to 112 pixels
        transforms.Resize(224),             # resize shortest side to 224 pixels
        transforms.CenterCrop(224),         # crop longest side to 224 pixels at center
    
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
])



######################################################################

transform=transforms.Compose([
        #transforms.RandomRotation(10),      # rotate +/- 10 degrees
        #transforms.RandomHorizontalFlip(),  # reverse 50% of images
        transforms.Resize(224),             # resize shortest side to 224 pixels
        transforms.CenterCrop(224),         # crop longest side to 224 pixels at center
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
])

---------------------------------------------------------------------

Compose(
    Resize(size=224, interpolation=bilinear, max_size=None, antialias=warn)
    CenterCrop(size=(224, 224))
    ToTensor()
    Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
)

######################################################################

image_path='/kaggle/input/world-championship-2023-embryo-classification/hvwc23/test/D3_205.jpg'
image = Image.open(image_path)
image = transform(image) 
plt.imshow(np.transpose(image.numpy(),(1,2,0))) 

######################################################################
