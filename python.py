#!/usr/bin/python3

import cgi, cgitb
import os
#mysql database connectivity

import mysql.connector

mydb = mysql.connector.connect(
  host="data",
  user="root",
  passwd="redhat123",
  database="register"
)

mycursor = mydb.cursor()
mycursor.execute("select * from register")
myresult = mycursor.fetchall() # it gives the list

# Create instance of FieldStorage
print ("Content-Type: text/html\n")

form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('Username')
password  = form.getvalue('Password')


for row in myresult:
        if (username == row[0]):
                print("Username already exists")
#        else:
 #               print("Success")

def data_entry():
    name = username
    pass1 = password
    mycursor.execute("INSERT INTO register(username, password) VALUES (%s,%s)", (name,pass1))
    print("<pre><h2>Successfully Registered</h2></pre>")
    mydb.commit()

#print("<pre><h2>Successfully Registered</h2></pre>")

#create_table()
data_entry()

