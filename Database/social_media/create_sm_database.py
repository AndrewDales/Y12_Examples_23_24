import sqlite3

create_users_table = """ 
CREATE TABLE IF NOT EXISTS users ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name TEXT NOT NULL, 
  age INTEGER, 
  gender TEXT, 
  nationality TEXT 
); 
"""

create_posts_table = """ 
CREATE TABLE IF NOT EXISTS posts( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,  
  title TEXT NOT NULL,  
  description TEXT NOT NULL,  
  user_id INTEGER NOT NULL,  
  FOREIGN KEY (user_id) REFERENCES users (id) 
); 
"""

create_likes_table = """ 
CREATE TABLE IF NOT EXISTS likes ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,  
  user_id INTEGER NOT NULL,  
  post_id integer NOT NULL,  
  FOREIGN KEY (user_id) REFERENCES users (id), 
  FOREIGN KEY (post_id) REFERENCES posts (id) 
); 
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  comment_text TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

# Create a connection to a database - if one does not exist, a new one will be created
conn = sqlite3.connect("sm_app.sqlite")

# A cursor is a pointer to a place in the database which allows access
# to a table row-by-row
cursor = conn.cursor()

try:
    cursor.execute(create_users_table)
    cursor.execute(create_posts_table)
    cursor.execute(create_likes_table)
    cursor.execute(create_comments_table)
finally:
    conn.close()
