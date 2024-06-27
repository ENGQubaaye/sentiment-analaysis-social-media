
import streamlit as st

import pickle 
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from streamlit_extras.let_it_rain import rain
ps = PorterStemmer()

import base64
from PIL import Image
import re
from sklearn.pipeline import Pipeline
# Read text from the 'data.txt' file
with open('data.txt', 'r') as file:
    default_text = file.read()

icon = Image.open('./1.png') #ico extnsion

st.set_page_config(
	page_title = 'PREDICTIO',
	page_icon = icon,
	layout = 'wide', #wide
	initial_sidebar_state = 'auto', #collapsed, expanded
	menu_items={
		'Get Help': 'https://streamlit.io',
		'Report a bug': 'https://github.com',
		'About':'About your application: *Hello World!*'
	}
	)





page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{

background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
primaryColor="#d8e00e"
backgroundColor="#1e64b7"
secondaryBackgroundColor="#1d1d1e"
textColor="#fdfdfd"

}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}

[data-testid="stSidebar"] > div:first-child {{

background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

</style>
"""
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('Somali') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Sentiment Analaysis Somali On Social Media ")

input_sms = st.text_area("Enter the message")





if st.button('Predict'):
     # 1. preprocess

    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    vector_input = vector_input.toarray()
    # print(default_text.find(i))
    # print(default_text)
    if not input_sms:
        st.header(" please enter a data")
    elif input_sms in default_text:
        st.header("Posotive - data")

    else:
        
    # 3. predict
     result = model.predict(vector_input)[0]
     
     if result == 0:
        st.header("Nagetive - data")



       
     else:
        st.header("Posotive - data")

    # 4. Display
    
    

       

   





