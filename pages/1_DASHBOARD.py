import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from joblib import Parallel, delayed
import base64
from PIL import Image
import preprocess  # Assuming this is your custom preprocessing module

# Load the icon image for the page
icon = Image.open('./1.png') 
# Set Streamlit page configuration
st.set_page_config(
    page_title='DASHBOARD',
    page_icon=icon,
    layout='wide',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io',
        'Report a bug': 'https://github.com',
        'About': 'About your application: *Hello World!*'
    }
)

# Function to train and evaluate a model
def train_evaluate_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    return accuracy, precision, recall, f1



# Read the dataset from a CSV file
df = pd.read_csv('last1.csv')

# Preprocess the dataset
df = preprocess.preprocess(df)

# Initialize TfidfVectorizer
tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(df['text']).toarray()
y = df['target'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Define models
models = {
    'Multinomial NB': MultinomialNB(),
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'SVM': SVC(),
    'Decision Tree': DecisionTreeClassifier(),
    'Gaussian NB': GaussianNB(),
    'Bernoulli NB': BernoulliNB(),
    'Random Forest': RandomForestClassifier(),
    'AdaBoost': AdaBoostClassifier(),
    'Extra Trees': ExtraTreesClassifier(),
    'KNeighbors': KNeighborsClassifier()
}

# Train and evaluate models in parallel
results = Parallel(n_jobs=-1)(delayed(train_evaluate_model)(model, X_train, y_train, X_test, y_test) for model in models.values())

# Extract results
accuracy_list, precision_list, recall_list, f1_list = zip(*results)

# Bar chart visualization
model_list = list(models.keys())
fig11 = px.bar(x=model_list, y=accuracy_list, color=model_list)
fig11.update_layout(title="Accuracy Comparison of Different Models", xaxis_title="Model", yaxis_title="Accuracy", font=dict(size=18))

# Sample data (you can replace these with your actual data)
total_data = 8124
Positive_date = 5001
negative_date = 3124
total_words_positive = 190129
total_words_negative = 79221
total_words_date = 269350

# Row A
st.markdown('### All Information')
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown('<div style="background-color: #ffdddd; padding: 10px; border-radius: 5px;">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #333;'>Total Data: <span style='color: red;'>{total_data}</span></h3>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div style="background-color: #ddffdd; padding: 10px; border-radius: 5px;">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #333;'>Positive Date: <span style='color: green;'>{Positive_date}</span></h3>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div style="background-color: #ddddff; padding: 10px; border-radius: 5px;">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #333;'>Negative Date: <span style='color: blue;'>{negative_date}</span></h3>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div style="background-color: #ffffdd; padding: 10px; border-radius: 5px;">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #333;'>Total Words of Positive: <span style='color: orange;'>{total_words_positive}</span></h3>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div style="background-color: #ddffff; padding: 10px; border-radius: 5px;">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #333;'>Total Words of Negative: <span style='color: teal;'>{total_words_negative}</span></h3>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div style="background-color: #ffddff; padding: 10px; border-radius: 5px;">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #333;'>Total Words in Date: <span style='color: purple;'>{total_words_date}</span></h3>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


c1, c2 = st.columns((7, 3))
with c1:
    st.markdown('### Accuracy Comparison of Different Models')
    st.plotly_chart(fig11)

with c2:
    st.markdown('### percentage of data')
    import helper  # Assuming this is your custom module
    x, new_df = helper.most_vis_data(df)
    fig, ax = plt.subplots()
    plt.pie(df['target'].value_counts(), labels=['POSITIVE', 'NEGATIVE'], autopct="%0.2f", colors=['orange', 'red'])
    plt.show()
    plt.xticks(rotation='vertical')
    st.pyplot(fig)

target_text_col1, target_text_col2 = st.columns(2)

with target_text_col1:
    st.markdown('#### Target Distribution')
    target_distribution = df['target'].value_counts().reset_index()
    target_distribution.columns = ['target', 'count']
    target_bar_chart = alt.Chart(target_distribution).mark_bar().encode(
        x='target',
        y='count'
    )
    st.altair_chart(target_bar_chart, use_container_width=True)

with target_text_col2:
    st.markdown('#### Sample Text Data')
    st.dataframe(df[['target', 'text']].head(10))