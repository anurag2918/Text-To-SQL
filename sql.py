import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute("INSERT INTO STUDENT VALUES('Sanya', 'ML', 'B', 85)")
cursor.execute("INSERT INTO STUDENT VALUES('Dev', 'AI', 'B', 53)")
cursor.execute("INSERT INTO STUDENT VALUES('Anika', 'ML', 'A', 94)")
cursor.execute("INSERT INTO STUDENT VALUES('Neeraj', 'AI', 'A', 39)")
cursor.execute("INSERT INTO STUDENT VALUES('Simran', 'ML', 'B', 79)")
cursor.execute("INSERT INTO STUDENT VALUES('Meera', 'ML', 'B', 77)")
cursor.execute("INSERT INTO STUDENT VALUES('Karan', 'AI', 'A', 42)")
cursor.execute("INSERT INTO STUDENT VALUES('Ishaan', 'ML', 'A', 88)")
cursor.execute("INSERT INTO STUDENT VALUES('Riya', 'AI', 'A', 64)")
cursor.execute("INSERT INTO STUDENT VALUES('Arjun', 'ML', 'A', 91)")

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()