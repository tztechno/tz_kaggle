
import pyctcdecode
import kenlm
import typing as tp
from typing import Any, Dict, List, Optional, Union
from pathlib import Path
from functools import partial
from dataclasses import dataclass, field
from bnunicodenormalizer import Normalizer
import cloudpickle as cpkl
from peft import LoraConfig, PeftModel, LoraModel, LoraConfig, get_peft_model
from abc import ABC, abstractmethod
from IPython.display import FileLink
import joblib
import whisper
import soundfile 
import jiwer
from concurrent.futures import ThreadPoolExecutor


#keras
from keras.models import Model
from keras.layers import Activation
from keras.layers import BatchNormalization
from keras.layers import Concatenate
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import GlobalAveragePooling2D
from keras.layers import Input
from keras.layers import Lambda
from keras.layers import MaxPooling2D
from keras.layers import add
from keras import backend as K


#transformers
from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments
from transformers import TrainingArguments
from transformers import TrainerState, TrainerControl, TrainerCallback
from transformers import WhisperFeatureExtractor
from transformers import Wav2Vec2Processor, Wav2Vec2ProcessorWithLM, Wav2Vec2ForCTC
from transformers import T5Tokenizer, T5ForConditionalGeneration


#sklearn
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_absolute_error, make_scorer
from sklearn.preprocessing import LabelEncoder,Normalizer
from sklearn.svm import SVC


#keras
from keras.models import Model
from keras.layers import Activation
from keras.layers import BatchNormalization
from keras.layers import Concatenate
from keras.layers import GlobalAveragePooling2D
from keras.layers import Input
from keras.layers import Lambda
from keras.layers import add
from keras import backend as K


#torch
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.distributed import init_process_group, destroy_process_group
import torch.multiprocessing as mp
import torchaudio
import torchaudio.transforms as tat


# Data manipulation
import polars as pl
pd.set_option("display.max_columns", None)


# Data visualization
from skimpy import skim


# Stats
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pingouin as pg
import ppscore as pps
