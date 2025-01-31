'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''
'''
Working with MySQL:
First, I created a database in MySQL worksheet, called 'arta', with the
'people' table, with the 'name', 'sex', and 'age' columns.
Now I want to connect from Python to MySQL.
'''

#Initially, using mysql, i created this small database:
# +-------+------+------+
# | name  | sex  | age  |
# +-------+------+------+
# | arta  | f    |   26 |
# | sarah | f    |   40 |
# | mehr  | m    |   34 |
# +-------+------+------+
#Now i want to add to this database using Python.

import mysql.connector 
#For installing this use py -m pip install mysql-connector

print('Connecting to DB')
cnx = mysql.connector.connect(user='user', password='password',
                              host='127.0.0.1',
                              database='arta')
print('Connected to DB') #To make sure I'm connected to the database.

name = 'hasan'; age = 12; sex = 'u' #unknown

cursor = cnx.cursor() #defining a variable called cursor which points to the DB
#input1:
# cursor.execute("INSERT INTO people VALUES (\'far\',\'f\',35)")
#input2:
cursor.execute("INSERT INTO people VALUES (\'%s\',\'%s\',%i)" % (name,sex,age))
#adding to the database
cnx.commit() #commiting for occurrence
cnx.close()

#output : 
# +-------+------+------+
# | name  | sex  | age  |
# +-------+------+------+
# | arta  | f    |   26 |
# | sarah | f    |   40 |
# | mehr  | m    |   34 |
# | far   | f    |   35 |
# +-------+------+------+

#output 2:
# +-------+------+------+
# | name  | sex  | age  |
# +-------+------+------+
# | arta  | f    |   26 |
# | sarah | f    |   40 |
# | mehr  | m    |   34 |
# | far   | f    |   35 |
# | hasan | u    |   12 |
# +-------+------+------+

''''''''''''''''''''''''''''''''''''''''''
