
######################################################################
######################################################################
######################################################################
######################################################################
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

######################################################################

image_path='/kaggle/input/world-championship-2023-embryo-classification/hvwc23/test/D3_205.jpg'
image = Image.open(image_path)
print(type(image)) ################################# type<class 'PIL.JpegImagePlugin.JpegImageFile'>
image = transform(image) ########################### transform成功
plt.imshow(np.transpose(image.numpy(),(1,2,0))) ########## transposeの方法

######################################################################
