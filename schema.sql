CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    join_date DATE
);

CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id INT,
    content TEXT,
    post_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE likes (
    like_id SERIAL PRIMARY KEY,
    user_id INT,
    post_id INT,
    like_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
);

CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    user_id INT,
    post_id INT,
    comment_text TEXT,
    comment_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
);