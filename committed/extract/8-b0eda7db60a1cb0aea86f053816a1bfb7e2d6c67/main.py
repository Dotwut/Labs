import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="", # Username Goes Here
  password="" # Password Goes Here
)

print(mydb)

