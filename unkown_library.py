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

from abc import ABC, abstractmethod



