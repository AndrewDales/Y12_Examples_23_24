import sqlite3

conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

select_students = """ 
SELECT id, firstname, lastname 
FROM students 
WHERE age >= 15 
"""

average_query = """ 
SELECT avg(age) 
FROM students 
WHERE gender = ? 
"""

group_by_query = """ 
SELECT gender, avg(age) 
FROM students 
GROUP BY gender 
"""

# Exercises
first_name_j_query = """
SELECT firstname, lastname
FROM students
WHERE firstname LIKE 'J%'
ORDER BY lastname ASC
LIMIT 5
"""

number_by_gender_query = """
SELECT gender, count(gender)
FROM students
GROUP BY gender
"""

age_by_first_letter_query = """
SELECT SUBSTR(firstname, 1,1), avg(age)
FROM students
GROUP BY SUBSTR(firstname, 1,1)
"""
try:
    cursor.execute(select_students)
    first_student = cursor.fetchone()
    more_students = cursor.fetchmany(10)
    other_students = cursor.fetchall()

    average_age_female = cursor.execute(average_query, ('female',)).fetchone()[0]
    average_age_by_gender = cursor.execute(group_by_query).fetchall()

    firstname_j = cursor.execute(first_name_j_query).fetchall()
    count_by_gender = cursor.execute(number_by_gender_query).fetchall()
    age_by_first_letter = cursor.execute(age_by_first_letter_query).fetchall()
finally:
    conn.close()
