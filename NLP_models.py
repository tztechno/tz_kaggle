
tokenizer = transformers.BertTokenizer.from_pretrained("bert-base-uncased")
model = transformers.BertForSequenceClassification.from_pretrained("bert-base-uncased",num_labels=1)


tokenizer = transformers.RobertaTokenizer.from_pretrained("roberta-base")
model = transformers.RobertaForSequenceClassification.from_pretrained("roberta-base",num_labels=1)


tokenizer = transformers.DebertaTokenizer.from_pretrained("microsoft/deberta-base")
model = transformers.DebertaForSequenceClassification.from_pretrained("microsoft/deberta-base",num_labels=1)


#delete token_type_ids in RoBERTa/DeBERTa
token_type_ids = torch.tensor(bert_sens['token_type_ids'], dtype=torch.long)



