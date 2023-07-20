#########################################################

#install into /kaggle/working/

!git clone https://github.com/JonathonLuiten/TrackEval.git /kaggle/working/TrackEval

#########################################################

!pip install pystan==2.19.1.1
!pip install fbprophet
import sys
sys.path.append('../input/multi-prophet/multi-prophet-master')
from multi_prophet import MultiProphet

#########################################################
