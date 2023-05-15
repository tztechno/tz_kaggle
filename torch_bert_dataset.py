
#####################################################

class BERTDataSet(Dataset):
    
    def __init__(self,sentences,targets):        
        self.sentences = sentences
        self.targets = targets
        
    def __len__(self):        
        return len(self.sentences)
    
    def __getitem__(self,idx):        
        sentence = self.sentences[idx]       
        bert_sens = tokenizer.encode_plus(
                                sentence,
                                add_special_tokens = True, 
                                max_length = max_sens, 
                                pad_to_max_length = True, 
                                return_attention_mask = True)

        ids = torch.tensor(bert_sens['input_ids'], dtype=torch.long)
        mask = torch.tensor(bert_sens['attention_mask'], dtype=torch.long)
        token_type_ids = torch.tensor(bert_sens['token_type_ids'], dtype=torch.long)     
        target = torch.tensor(self.targets[idx],dtype=torch.float)
        
        return {
                'ids': ids,
                'mask': mask,
                'token_type_ids': token_type_ids,
                'targets': target
            }

#####################################################

class RoBERTaDataSet(Dataset):
    
    def __init__(self, sentences, targets):        
        self.sentences = sentences
        self.targets = targets
        
    def __len__(self):        
        return len(self.sentences)
    
    def __getitem__(self, idx):        
        sentence = self.sentences[idx]
        
        bert_sens = tokenizer.encode_plus(
            sentence,
            add_special_tokens=True, 
            max_length=max_sens, 
            padding='max_length', 
            return_attention_mask=True,
            return_tensors='pt'
        )

        input_ids = bert_sens['input_ids'].squeeze()
        attention_mask = bert_sens['attention_mask'].squeeze()
        target = torch.tensor(self.targets[idx], dtype=torch.float)
        
        return {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'targets': target
        }
      
#####################################################


#####################################################
