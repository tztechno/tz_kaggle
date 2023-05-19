from super_gradients import Trainer

from super_gradients.training import Trainer
from super_gradients.training import training_hyperparams
from super_gradients.training import models
from super_gradients.training import dataloaders
from super_gradients.training import metrics
from super_gradients.training.utils import sg_model_utils

from super_gradients.training.datasets import DatasetInterface
from super_gradients.training.datasets import datasets_utils, DataAugmentation, DetectionDataSet, TestDatasetInterface
from super_gradients.training.datasets import Cifar10
from super_gradients.training.datasets import ImageNetDataset
from super_gradients.training.datasets import COCODetectionDataset
from super_gradients.training.datasets import PascalVOCDetectionDataset
from super_gradients.training.datasets import YoloDarknetFormatDetectionDataset
from super_gradients.training.datasets import CityscapesDataset
from super_gradients.training.datasets import CoCoSegmentationDataSet

from super_gradients.training.models import ARCHITECTURES
from super_gradients.training.losses import LOSSES
from super_gradients.training.exceptions.sg_model_exceptions import UnsupportedOptimizerFormat

from super_gradients.common.object_names import Datasets
from super_gradients.common.registry.registry import register_dataset
from super_gradients.common.abstractions.abstract_logger import get_logger





# onject detection

url = "https://previews.123rf.com/images/freeograph/freeograph2011/freeograph201100150/158301822-group-of-friends-gathering-around-table-at-home.jpg"
yolo_nas_l.predict(url, conf=0.25).show()

# semantic segmentation


# image classification








