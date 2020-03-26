import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)

mycursor = mydb.cursor()
data=input("Enter Name")

sql = "INSERT INTO testuser (name, age) VALUES ('"+data+"', '31')"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")