
#################################

Name=data['Species'].unique().tolist()

#################################

dataset0=datasets.ImageFolder(root="/kaggle/input/flower-photos-by-the-tensorflow-team/flower_photos",transform=None)
class_names=dataset0.classes

#################################

