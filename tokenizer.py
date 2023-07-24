#########################################################

def create_data(text):
    encoded = tokenizer.batch_encode_plus(
        text,
        add_special_tokens = True,
        max_length= max_len,
        padding='max_length',
        truncation=True,
        return_attention_mask=True)

    input_ids       = np.array(encoded["input_ids"], dtype="int32")
    attention_masks = np.array(encoded["attention_mask"], dtype="int32")

    return {"input_ids": input_ids, "attention_masks": attention_masks}
  
#########################################################

この関数は、与えられたtextをトークン化し、エンコードして、入力として使用できる形式に変換します。
トークン化は、与えられたテキストを小さなトークンに分割するプロセスです。
エンコードは、各トークンに対応する数値IDに変換するプロセスです。入力として使用できる形式に変換するために、
input_idsとattention_masksという2つのNumPy配列が作成されます。

input_idsは、エンコードされたトークンの数値IDの配列です。この配列は、モデルに入力するテキストデータの部分です。

attention_masksは、モデルが注意を払うべきトークンを示すバイナリマスクの配列です。
つまり、パディングされたトークン（テキストの短いシーケンスを最大長に拡張するために追加されたトークン）は、
モデルが無視する必要があるため、0でマスクされます。一方、元のテキストに含まれるトークンは、1でマスクされます。
  
#########################################################  

import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import transformers
from transformers import BertTokenizer, TFBertModel
transformers.logging.set_verbosity_error()

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased') #from huggingface bert-base-uncased 
max_len = 128

def create_data(text):
    encoded = tokenizer.batch_encode_plus(
        text,
        add_special_tokens = True,
        max_length= max_len,
        padding='max_length',
        truncation=True,
        return_attention_mask=True)

    input_ids       = np.array(encoded["input_ids"], dtype="int32")
    attention_masks = np.array(encoded["attention_mask"], dtype="int32")

    return {"input_ids": input_ids, "attention_masks": attention_masks}

train_data = create_data(train_df['text'][0:10])
  
#########################################################  
