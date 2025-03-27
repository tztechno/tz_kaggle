##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
[model standard form for training]

        # Get current example
        inputs = self.train_env.get_current_input()
        target_ids = self.train_env.get_current_target()
        
        # Forward pass with teacher forcing for supervised learning
        outputs = self.model(
            input_ids=inputs['input_ids'],
            attention_mask=inputs['attention_mask'],
            labels=target_ids
        )
        
        # Calculate standard seq2seq loss (teacher forcing loss)
        loss = outputs.loss

##############################################
[deepseek r1 training ]

    def get_current_input(self):
        """
        Get current input for the model, adapting from existing preprocess_function
        """
        questions = self.questions[self.current_idx]
        
        # DeepSeek R1 specific input formatting
        inputs = f"Question: {questions}"
        
        # Tokenize with similar parameters to original preprocess_function
        encoding = self.tokenizer(
            inputs, 
            return_tensors='pt', 
            truncation=True, 
            max_length=self.max_length,  # Use class-defined max length
            padding='max_length'
        )
        
        return {k: v.to(device) for k, v in encoding.items()}
    
    def get_current_target(self):
        """
        Get current target for the model, adapting from existing preprocess_function
        """
        answers = self.answers[self.current_idx]
        
        # Tokenize target with similar parameters
        target_encoding = self.tokenizer(
            text_target=answers, 
            return_tensors='pt', 
            truncation=True, 
            max_length=self.max_length,
            padding='max_length'
        )
        
        return target_encoding['input_ids'].to(device)
      
##############################################
[T5 training loop]

    def get_current_input(self):
        question = self.questions[self.current_idx]
        # For T5, prefix the input with a task-specific prefix
        encoding = self.tokenizer(f"answer: {question}", return_tensors='pt', truncation=True, max_length=128)
        return {k: v.to(device) for k, v in encoding.items()}

    def get_current_target(self):
        answer = self.answers[self.current_idx]
        target_encoding = self.tokenizer(text_target=answer, return_tensors='pt', truncation=True, max_length=128)
        return target_encoding['input_ids'].to(device)
      
##############################################
