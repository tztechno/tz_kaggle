
## clean_text

import string
from nltk.corpus import stopwords

def clean_text(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

train['clean_text'] = train['short_description'].apply(clean_text)
test['clean_text'] = test['short_description'].apply(clean_text)

## remove_stopwords

stop_words = stopwords.words('english')
more_stopwords = ['u', 'im', 'c']
stop_words = stop_words + more_stopwords

def remove_stopwords(text):
    words = text.split(' ')
    words = [word for word in words if word not in stop_words]
    text = ' '.join(words)
    return text

train['clean_text'] = train['clean_text'].apply(remove_stopwords)
test['clean_text'] = test['clean_text'].apply(remove_stopwords)

##  stemm_text

import nltk

stemmer = nltk.SnowballStemmer("english")

def stemm_text(text):
    text = ' '.join(stemmer.stem(word) for word in text.split(' '))
    return text

train['clean_text'] = train['clean_text'].apply(stemm_text)
test['clean_text'] = test['clean_text'].apply(stemm_text)

## preprocess_data

def preprocess_data(text):
    # Clean puntuation, urls, and so on
    text = clean_text(text)
    # Remove stopwords
    text = ' '.join(word for word in text.split(' ') if word not in stop_words)
    # Stemm all the words in the sentence
    text = ' '.join(stemmer.stem(word) for word in text.split(' '))
    return text

train['clean_text'] = train['clean_text'].apply(preprocess_data)
test['clean_text'] = test['clean_text'].apply(preprocess_data)
