import psycopg2
import pandas as pd
from textblob import TextBlob

conn = psycopg2.connect(
    dbname="social_media",
    user="postgres",
    password="abcd1234",
    host="localhost",
    port="5432"
)

query = "SELECT comment_id, comment_text FROM comments;"
df = pd.read_sql(query, conn)

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

df['sentiment'] = df['comment_text'].apply(get_sentiment)

print(df)

conn.close()