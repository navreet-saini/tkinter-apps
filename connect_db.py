import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="123456",
    database="internship"
)

cur=conn.cursor()
cur.execute("insert into student_info values(104,'bob','1234567891','xyz')")
cur.execute("insert into student_info values(105,'babita','12345678871','xyu')")
cur.execute("insert into student_info values(106,'david','12349876691','xyyu')")


conn.commit()