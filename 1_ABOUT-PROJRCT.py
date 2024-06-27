import streamlit as st

# Title
st.title("Sentiment Analysis of Social Media Comments in Somali using Machine Learning")

# Introduction
st.header("Introduction")
st.write("""
Sentiment analysis is a method of identifying and categorizing opinions expressed in a piece of text, 
especially to determine whether the writer's attitude towards a particular topic, product, etc., is positive, negative, or neutral. 
This thesis focuses on performing sentiment analysis on social media comments written in Somali using machine learning techniques.
""")

# Methodology
# st.header("Methodology")
# st.write("""
# The methodology involves several key steps:
# 1. *Data Collection*: Gathering a large dataset of social media comments written in Somali.
# 2. *Data Preprocessing*: Cleaning and preparing the data for analysis, including text normalization and removal of stop words.
# 3. *Feature Extraction*: Converting text data into numerical features that can be used by machine learning models.
# 4. *Model Training*: Training machine learning models using labeled data to classify the sentiment of comments.
# 5. *Evaluation*: Assessing the performance of the models using metrics like accuracy, precision, recall, and F1-score.
# """)

# Data Collection
# st.subheader("Data Collection")
# st.write("""
# Data was collected from various social media platforms where users frequently post comments in Somali. 
# The collected data was then labeled manually to indicate the sentiment (positive, negative, or neutral).
# """)

# Data Preprocessing
# st.subheader("Data Preprocessing")
# st.write("""
# Preprocessing involved the following steps:
# - Text normalization: Converting all text to lowercase, removing punctuation, and handling special characters.
# - Tokenization: Splitting text into individual words or tokens.
# - Stop words removal: Removing common words that do not contribute to the sentiment.
# - Lemmatization: Reducing words to their base or root form.
# """)

# Feature Extraction
# st.subheader("Feature Extraction")
# st.write("""
# Feature extraction techniques used include:
# - *Bag of Words (BoW)*: Representing text as a set of independent words.
# - *TF-IDF (Term Frequency-Inverse Document Frequency)*: Reflecting the importance of a word in a document relative to a collection of documents.
# - *Word Embeddings*: Using pre-trained models like Word2Vec or GloVe to capture the semantic meaning of words.
# """)

# Model Training
# st.subheader("Model Training")
# st.write("""
# Several machine learning algorithms were used for training, including:
# - *Logistic Regression*: A simple yet effective linear model for binary classification.
# - *Support Vector Machines (SVM)*: A powerful model for classification tasks.
# - *Random Forest*: An ensemble method that combines multiple decision trees.
# - *Recurrent Neural Networks (RNNs)*: Deep learning models, particularly LSTM and GRU, to capture sequential dependencies in text data.
# """)

# Evaluation
# st.subheader("Evaluation")
# st.write("""
# The models were evaluated using various metrics:
# - *Accuracy*: The proportion of correctly classified instances.
# - *Precision*: The proportion of true positive instances among the predicted positive instances.
# - *Recall*: The proportion of true positive instances among the actual positive instances.
# - *F1-Score*: The harmonic mean of precision and recall.
# """)

# Results
# st.header("Results")
# st.write("""
# The results showed that deep learning models, specifically LSTM, outperformed traditional machine learning models in terms of accuracy and F1-score. 
# The following table summarizes the performance metrics of the different models:
# """)



# Conclusion
# st.header("Conclusion")
# st.write("""
# The study demonstrates that machine learning techniques can effectively perform sentiment analysis on social media comments in Somali. 
# Deep learning models, particularly LSTM, provide superior performance compared to traditional methods. 
# Future work may involve expanding the dataset and exploring more advanced models to further improve the accuracy and robustness of the sentiment analysis system.
# """)