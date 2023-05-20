import mysql.connector
from flask import Flask
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
 password= None,
 database="facebook"
)
print(mydb)

