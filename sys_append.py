###########################################

#### after pip download ultralytics

import sys
sys.path.append('/kaggle/input/pip-download-ultralytics')
!pip install /kaggle/input/your-dataset-name/ultralytics-*.whl

###########################################

import sys
sys.path.append('../input/multi-prophet/multi-prophet-master')
from multi_prophet import MultiProphet

###########################################

sys.path.append("/kaggle/input/detection-wheel")

#/kaggle/input/detection-wheelディレクトリ内にmy_module.pyというPythonモジュールがある場合
import my_module

###########################################
