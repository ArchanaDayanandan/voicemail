import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM testuser")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)