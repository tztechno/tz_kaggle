...from_pretrained(model_name,num_labels=2)
output = output["logits"].detach()[:,1].reshape((-1))


#/kaggle/input/roberta-base
...from_pretrained(model_name,num_labels=1)
output = output["logits”].squeeze(-1)


#/kaggle/input/transformers-roberta-base
config = transformers.RobertaConfig.from_pretrained(model_name)
config.num_labels = 1
model = ...from_pretrained(model_name,config=config, ignore_mismatched_sizes=True)#for num_labels=1
out_features=1への修正に成功
