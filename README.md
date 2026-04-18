# Twitter Analytics System

## Project Overview

This project is a Twitter-style Social Media Analytics System that stores user activity in a PostgreSQL database and performs analysis using SQL and AI.

It includes:

* Data storage using PostgreSQL
* Analytics using SQL queries
* Sentiment analysis using Python (TextBlob)
* Interactive dashboard using Streamlit

---

## Features

* User, Tweet, Like, and Comment system
* SQL-based analytics (engagement, likes, activity)
* Sentiment analysis on tweets/comments
* Interactive dashboard with metrics and charts

---

## Tech Stack

* Database: PostgreSQL
* Backend: Python
* Frontend: Streamlit
* Libraries: pandas, psycopg2, TextBlob

---

## Project Structure

```
app.py                  # Streamlit dashboard
load_data.py            # Loads dataset into PostgreSQL
sentiment_analysis.py   # AI sentiment analysis
tweets.csv              # Dataset (input data)
schema.sql              # Database schema
requirements.txt        # Dependencies
README.md               # Project documentation
```

---

## Dataset

A CSV dataset (`tweets.csv`) containing tweet text is used.
This dataset is loaded into PostgreSQL using `load_data.py`.

---

## Setup Instructions

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Setup PostgreSQL

* Install PostgreSQL
* Create database:

```
CREATE DATABASE social_media;
```

### 3. Create Tables

Run the SQL commands from:

```
schema.sql
```

### 4. Load Dataset

```
python load_data.py
```

### 5. Run Application

```
python -m streamlit run app.py
```

---

## AI Component

Sentiment analysis is performed using TextBlob, which classifies text as:

* Positive
* Neutral
* Negative

---

## Output

The dashboard displays:

* Total Users, Posts, Likes, Comments
* Engagement metrics
* Sentiment distribution
* Graphs and analytics

---

## Key Learning

* Database design with foreign keys
* SQL analytics queries
* Integration of AI with databases
* Building dashboards using Streamlit

---

## Future Improvements

* Add user authentication
* Real-time data streaming
* Deploy using cloud database

---

## Author

Shashwat Mishra
