import streamlit as st
import psycopg2
import pandas as pd
from textblob import TextBlob

# Page config
st.set_page_config(page_title="Social Media Analytics", layout="wide")

# Connect DB
conn = psycopg2.connect(
    dbname="social_media",
    user="postgres",
    password="abcd1234",
    host="localhost",
    port="5432"
)

# Title
st.title("📊 Social Media Analytics System")

# Sidebar navigation
option = st.sidebar.selectbox(
    "Select View",
    ["Dashboard", "Users", "Posts", "Likes", "Comments + AI"]
)

# -------- DASHBOARD --------
if option == "Dashboard":
    st.subheader("Overview Dashboard")

    users = pd.read_sql("SELECT * FROM users;", conn)
    posts = pd.read_sql("SELECT * FROM posts;", conn)
    likes = pd.read_sql("SELECT * FROM likes;", conn)
    comments = pd.read_sql("SELECT * FROM comments;", conn)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Users", len(users))
    col2.metric("Posts", len(posts))
    col3.metric("Likes", len(likes))
    col4.metric("Comments", len(comments))

    st.subheader("Likes per Post")
    likes_data = pd.read_sql("""
        SELECT post_id, COUNT(*) AS total_likes
        FROM likes
        GROUP BY post_id
        ORDER BY total_likes DESC;
    """, conn)

    st.bar_chart(likes_data.set_index("post_id"))

# -------- USERS --------
elif option == "Users":
    st.subheader("Users Data")
    users = pd.read_sql("SELECT * FROM users;", conn)
    st.dataframe(users)

# -------- POSTS --------
elif option == "Posts":
    st.subheader("Posts Data")
    posts = pd.read_sql("SELECT * FROM posts;", conn)
    st.dataframe(posts)

# -------- LIKES --------
elif option == "Likes":
    st.subheader("Likes Data")
    likes = pd.read_sql("SELECT * FROM likes;", conn)
    st.dataframe(likes)

# -------- COMMENTS + AI --------
elif option == "Comments + AI":
    st.subheader("Comments with Sentiment Analysis")

    comments = pd.read_sql("SELECT comment_id, comment_text FROM comments;", conn)

    def get_sentiment(text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return "Positive"
        elif analysis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negative"

    comments['sentiment'] = comments['comment_text'].apply(get_sentiment)

    st.dataframe(comments)

    st.subheader("Sentiment Distribution")
    st.bar_chart(comments['sentiment'].value_counts())

# Close connection
conn.close()