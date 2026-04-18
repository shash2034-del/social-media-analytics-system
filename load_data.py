import psycopg2
import pandas as pd

# Load CSV
df = pd.read_csv("tweets.csv")

# Take only 20–50 rows
df = df.head(20)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="social_media",
    user="postgres",
    password="abcd1234",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Insert data
for i, row in df.iterrows():
    text = row['text']
    
    cursor.execute("""
        INSERT INTO comments (user_id, post_id, comment_text, comment_date)
        VALUES (%s, %s, %s, CURRENT_DATE)
    """, (1, 1, text))

conn.commit()
cursor.close()
conn.close()

print("Real Twitter data inserted!")