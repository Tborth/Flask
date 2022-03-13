print("hello")
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",               #hostname
  user="root",                   # the user who has privilege to the db
  passwd="webkul123",               #password for user
  database="python1",               #database name
    auth_plugin = 'mysql_native_password',

)
print(mydb)
mydbcuesor =mydb.cursor()
mydbcuesor.execute("show databases")
print(mydbcuesor)
for i in mydbcuesor:
    print(i)