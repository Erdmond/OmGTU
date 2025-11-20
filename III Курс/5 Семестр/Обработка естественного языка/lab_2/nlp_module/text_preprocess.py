import pymorphy3
from nltk.corpus import stopwords
import re
from razdel import tokenize

morph = pymorphy3.MorphAnalyzer()
russian_stopwords = set(stopwords.words('russian'))

def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+|www\.\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[^а-яё\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def tokenize_with_razdel(text):
    return [token.text for token in tokenize(text)]

def lemmatize_tokens(tokens):
    lemmas = []
    for token in tokens:
        parsed = morph.parse(token)[0]
        lemma = parsed.normal_form
        lemmas.append(lemma)
    return lemmas

def remove_stopwords(tokens):
    return [token for token in tokens if token not in russian_stopwords and len(token) > 2]

def full_text_preprocessing(text):
    cleaned_text = preprocess_text(text)
    tokens = tokenize_with_razdel(cleaned_text)
    lemmas = lemmatize_tokens(tokens)
    filtered_lemmas = remove_stopwords(lemmas)
    
    return filtered_lemmas
