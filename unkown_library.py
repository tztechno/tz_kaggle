import pyctcdecode
import kenlm

import typing as tp
from typing import Any, Dict, List, Optional, Union

from pathlib import Path

from functools import partial

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
from dataclasses import dataclass, field

from bnunicodenormalizer import Normalizer
import cloudpickle as cpkl
from peft import LoraConfig, PeftModel, LoraModel, LoraConfig, get_peft_model

from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments
from transformers import TrainingArguments
from transformers import TrainerState, TrainerControl, TrainerCallback
from transformers import WhisperFeatureExtractor
from transformers import Wav2Vec2Processor, Wav2Vec2ProcessorWithLM, Wav2Vec2ForCTC
from transformers import T5Tokenizer, T5ForConditionalGeneration

import torchaudio
import torchaudio.transforms as tat

from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_absolute_error, make_scorer
from sklearn.preprocessing import LabelEncoder,Normalizer
from sklearn.svm import SVC

from abc import ABC, abstractmethod

from IPython.display import FileLink
import joblib

from keras.models import Model
from keras.layers import Activation
from keras.layers import BatchNormalization
from keras.layers import Concatenate
from keras.layers import GlobalAveragePooling2D
from keras.layers import Input
from keras.layers import Lambda
from keras.layers import add
from keras import backend as K
