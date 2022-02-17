#-----------------------------------------Create and Read-----------------------------------------------

import sqlite3
def sql_connection():
        conn = sqlite3.connect('Student.db')
        return conn

# def sql_table(conn):
#     cursorObj = conn.cursor()
#     cursorObj.execute("CREATE TABLE Student(student_id n(5), name char(30), class char(10), Score n(20));")
#     cursorObj.executescript("""
#    INSERT INTO Student VALUES(1,'Anirudh', '10th', 96);
#    INSERT INTO Student VALUES(2,'Rishab', '9th', 97);
#    INSERT INTO Student VALUES(3,'Rohit', '8th', 98);
#    INSERT INTO Student VALUES(4,'Virat', '7th', 99);
#    INSERT INTO Student VALUES(5,'Rahul', '6th', 94);
#    """)
#
#     conn.commit()
#     cursorObj.execute("SELECT * FROM Student")
#     rows = cursorObj.fetchall()
#     print("Student details:")
#     for row in rows:
#         print(row)

#------------------------------------Update and Read-------------------------------------------------------------------
# def sql_table(conn):
#     cursorObj = conn.cursor()
#     cursorObj.execute("SELECT * FROM Student")
#     rows = cursorObj.fetchall()
#     print("Student details:")
#     for row in rows:
#         print(row)
#     print("\nUpdate Score 96 to 100 where id is 1:")
#     sql_update_query = """Update Student set score = 100  where Student_id = 1"""
#     cursorObj.execute(sql_update_query)
#     conn.commit()
#     print("Record Updated successfully ")
#     cursorObj.execute("SELECT * FROM Student")
#     rows = cursorObj.fetchall()
#     print("\nAfter updating Student details:")
#     for row in rows:
#         print(row)

#-----------------------------------------------Delete and read----------------------------------------------------
def sql_table(conn):
   cursorObj = conn.cursor()
   cursorObj.execute("SELECT * FROM Student")
   rows = cursorObj.fetchall()
   print("Student details:")
   for row in rows:
       print(row)
   print("\nDelete Student of ID 3:")
   s_id = 3
   cursorObj.execute("""
   DELETE FROM Student
   WHERE student_id = ?
   """, (s_id,))
   conn.commit()
   cursorObj.execute("SELECT * FROM Student")
   rows = cursorObj.fetchall()
   print("\nAfter updating Student details:")
   for row in rows:
       print(row)


sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
 sqllite_conn.close()
 print("\nThe SQLite connection is closed.")
