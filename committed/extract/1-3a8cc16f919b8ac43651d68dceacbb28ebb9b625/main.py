import mysql.connector

def create_db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root", # Username Goes Here
    password="flag{a489a9dbf8eb9d37c6e0cc1a92cda17b}" # Password Goes Here
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE commited")


def create_tables():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root", #username Goes here
    password="flag{a489a9dbf8eb9d37c6e0cc1a92cda17b}", #password Goes here
    database="commited"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    

def populate_tables():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="flag{a489a9dbf8eb9d37c6e0cc1a92cda17b}",
    database="commited"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


create_db()
create_tables()
populate_tables()
