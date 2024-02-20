import sqlite3
from faker import Faker
import random

fake = Faker(['en_US', 'en_GB', 'it_IT'])

parameterised_insert_query = """
INSERT INTO 
    students (firstname, lastname, age, gender)
VALUES
    (?, ?, ?, ?);
"""

conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

fake.seed_instance(777)
random.seed(777)
data = [(fake.first_name(),
         fake.last_name(),
         random.randint(11, 18),
         random.choice(('male', 'female')))
        for _ in range(50)]

cursor.executemany(parameterised_insert_query, data)


conn.commit()
conn.close()
