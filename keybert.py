
!pip install keybert

from keybert import KeyBERT

doc = "Your input text goes here."

model = KeyBERT('distilbert-base-nli-mean-tokens')
keywords = model.extract_keywords(doc)

print(keywords)
