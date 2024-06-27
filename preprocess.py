import re
import pandas as pd
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
import nltk
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

def preprocess(df):
    
    

    df.rename(columns={'v1': 'target','v2': 'text'}, inplace=True)
    df['target'] = encoder.fit_transform(df['target'])
    # remove duplicates
    df = df.drop_duplicates(keep='first')
    df['num_characters'] = df['text'].apply(len)
    df['num_words'] = df['text'].apply(lambda x:len(nltk.word_tokenize(x)))
    df['num_sentences'] = df['text'].apply(lambda x:len(nltk.sent_tokenize(x)))

    

    
    

    return df


