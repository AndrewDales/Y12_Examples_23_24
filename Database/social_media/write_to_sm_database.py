import sqlite3

parameterised_insert_users_query = """
INSERT INTO 
    users (name, age, gender, nationality)
VALUES
    (?, ?, ?, ?);
"""

param_insert_posts_query = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  (?, ?, ?);
"""

param_insert_comments_query = """
INSERT INTO
  comments (comment_text, user_id, post_id)
VALUES
  (?, ?, ?);
"""

param_insert_likes_query = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (?, ?);
"""

data_users = [('James', 25, 'male', 'USA'),
              ('Leila', 32, 'female', 'France'),
              ('Brigitte', 35, 'female', 'England'),
              ('Mike', 40, 'male', 'Denmark'),
              ('Elizabeth', 21, 'female', 'Canada'),
              ]

data_posts = [('Happy', 'I am feeling very happy today', 1),
              ('Hot Weather', 'The weather is very hot today', 2),
              ('Help', 'I need some help with my work', 2),
              ('Great News', 'I am getting married', 1),
              ('Interesting Game', 'It was a fantastic game of tennis', 5),
              ('Party', 'Anyone up for a late-night party today?', 3),
              ]

data_comments = [('Count me in', 1, 6),
                 ('What sort of help?', 5, 3),
                 ('Congrats buddy', 2, 4),
                 ('I was rooting for Nadal though', 4, 5),
                 ('Help with your thesis?', 2, 3),
                 ('Many congratulations', 5, 4),
                 ]

data_likes = [(1, 6),
              (2, 3),
              (1, 5),
              (5, 4),
              (2, 4),
              (4, 2),
              (3, 6),
              ]

conn = sqlite3.connect("sm_app.sqlite")
cursor = conn.cursor()

try:

    # Insert users
    # cursor.executemany(parameterised_insert_users_query, data_users)
    # conn.commit()

    # Insert posts
    cursor.executemany(param_insert_posts_query, data_posts)
    conn.commit()

    # Insert comments
    cursor.executemany(param_insert_comments_query, data_comments)
    conn.commit()

    # Insert likes
    cursor.executemany(param_insert_likes_query, data_likes)
    conn.commit()

finally:
    conn.close()
