import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

students = [
    ('John', 'ML', 'A', 85),
    ('Jane', 'AI', 'B', 90),
    ('Doe', 'ML', 'A', 75),
    ('Alice', 'AI', 'A', 95),
    ('Bob', 'ML', 'B', 80),
    ('Joe', 'ML', 'B', 98),
    ('Jack', 'AI', 'A', 79),
]
cursor.executemany("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?);", students)

print("The inserted records are:")

data = cursor.execute("SELECT * FROM STUDENT;")
for row in data:
    print(row)

connection.commit()
connection.close()
