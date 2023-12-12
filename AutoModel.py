from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "roberta-base"
#config = AutoConfig.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)   

#tokenizer = transformers.RobertaTokenizer.from_pretrained("/kaggle/input/roberta-base")
#tokenizer = transformers.RobertaTokenizer.from_pretrained("roberta-base")
#model = AutoModelForSequenceClassification.from_pretrained(model_name)
#model = transformers.RobertaForSequenceClassification.from_pretrained("/kaggle/input/roberta-base",num_labels=1)
