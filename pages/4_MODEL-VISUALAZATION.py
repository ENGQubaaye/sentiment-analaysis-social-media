import numpy as np
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, classification_report
from sklearn.ensemble import AdaBoostClassifier, ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
import plotly.express as px
import plotly.figure_factory as ff
from PIL import Image

# Load and preprocess data
df1 = pd.read_csv('last.csv')
df = df1.drop_duplicates(keep='first')
df['text'] = df['text']

tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(df['text']).toarray()
y = df['target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize models
models = {
    "MultinomialNB": MultinomialNB(),
    "Logistic Regression": LogisticRegression(),
    "SVM": SVC(),
    "Decision Tree": DecisionTreeClassifier(),
    "GaussianNB": GaussianNB(),
    "BernoulliNB": BernoulliNB(),
    "RandomForest": RandomForestClassifier(),
    "AdaBoost": AdaBoostClassifier(),
    "ExtraTrees": ExtraTreesClassifier(),
    "KNeighbors": KNeighborsClassifier()
}

# Train and evaluate models
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    results[name] = {
        "accuracy": accuracy_score(y_test, y_pred),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "classification_report": classification_report(y_test, y_pred, target_names=['Positive', 'Negative'])
    }

# Streamlit configuration
icon = Image.open('./1.png')  # Ensure the correct path to your image file

st.set_page_config(
    page_title='MODEL-VISUALIZATION',
    page_icon=icon,
    layout='wide',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io',
        'Report a bug': 'https://github.com',
        'About': 'About your application: *Hello World!*'
    }
)

# Hide Streamlit default elements
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Display results in two columns
col1, col2 = st.columns(2)

color_scales = [
    'Blues', 'Greens', 'Reds', 'Purples', 'Oranges', 'Viridis', 'Cividis', 'Plasma', 'Magma', 'Inferno'
]

for i, (name, result) in enumerate(results.items()):
    if i % 2 == 0:
        col = col1
    else:
        col = col2
    
    col.subheader(f"{name} - Accuracy: {result['accuracy']:.4f}, Recall: {result['recall']:.4f}, F1 Score: {result['f1_score']:.4f}, Precision: {result['precision']:.4f}")
    fig = ff.create_annotated_heatmap(
        z=result['confusion_matrix'],
        x=['Positive', 'Negative'],
        y=['Negative', 'Positive'],
        colorscale=color_scales[i % len(color_scales)],
        showscale=True,
        annotation_text=[[f'FN = {result["confusion_matrix"][1, 0]}', f'TN = {result["confusion_matrix"][0, 0]}'], 
                         [f'TP = {result["confusion_matrix"][1, 1]}', f'FP = {result["confusion_matrix"][0, 1]}']],
        font_colors=['black', 'white'],
        hoverinfo='skip'
    )
    fig.update_layout(
        title=f"Confusion Matrix ({name})",
        xaxis=dict(title="Predicted"),
        yaxis=dict(title="Actual"),
        font=dict(size=12)
    )
    col.plotly_chart(fig)

    col.markdown(f"<pre>{result['classification_report']}</pre>", unsafe_allow_html=True)
    col.markdown("<br><br>", unsafe_allow_html=True)  # Adding space between visualizations

# Bar chart for accuracy comparison
accuracy_list = [result["accuracy"] for result in results.values()]
model_list = list(results.keys())
fig = px.bar(x=model_list, y=accuracy_list, color=model_list)
fig.update_layout(title="Accuracy Comparison of Different Models", xaxis_title="Model", yaxis_title="Accuracy", font=dict(size=18))
st.plotly_chart(fig)
