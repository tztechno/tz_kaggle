#peft setting for roberta

from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training, TaskType

# 2. モデルの準備（LoRA用）
model = prepare_model_for_kbit_training(model)

# 3. LoRAの設定
lora_config = LoraConfig(
    task_type=TaskType.SEQ_CLS,   # タスクタイプ（例: 文章分類）
    inference_mode=False,         # 推論モード（微調整時はFalse）
    r=8,                          # ランク
    lora_alpha=16,                # LoRAのスケーリング係数
    lora_dropout=0.1              # ドロップアウト率
)

# 4. LoRAの適用
lora_model = get_peft_model(model, lora_config)
model = lora_model
display(model)
