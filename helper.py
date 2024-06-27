from wordcloud import WordCloud
import pandas as pd
from collections import Counter



def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['target'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['text']:
        words.extend(message.split())

    

    num_characters = df[df['text'] == 'num_characters'].shape[1]


    return num_messages,len(words),num_characters


def most_vis_data(df):
    x = df['target'].value_counts().head()
    df = round((df['target'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'text', 'type': 'percent'})
    return x,df

def create_wordcloud(selected_user,df):
    f = open('Somali1.txt', 'r')
    stop_words1 = f.read()
    

    

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words1:
                y.append(word)
        return " ".join(y)

    if selected_user != 'Overall':
        df = df[df['target'] == selected_user]

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp=df['text'].apply(remove_stop_words)
    df_wc = wc.generate(temp.str.cat(sep=" "))
    
    return df_wc

def most_common_words(selected_user,df):

    f = open('Somali1.txt','r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['target'] == selected_user]

    words = []

    for message in df['text']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['target'] == selected_user]

    user_heatmap = df.pivot_table(index='target', columns='target', values='text', aggfunc='count').fillna(0)

    return user_heatmap

