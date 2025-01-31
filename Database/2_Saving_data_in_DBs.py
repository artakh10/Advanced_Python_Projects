'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''
'''
Now, I want to read and save data and information in my database.
If a row of data is repeated numerously, this is how one deletes it:
 DELETE FROM people WHERE name = 'name' LIMIT 'number';
'''
import mysql.connector 
cnx = mysql.connector.connect(user='user', password='oassword',
                              host='127.0.0.1',database = 'arta')
cursor = cnx.cursor()
query = 'SELECT * FROM people;'
cursor.execute(query)
gender = {'f':'Female', 'm':'Male', 'u':'Unknown'}
pronouns = {'f':'her','m':'his','u':'their'}
for (name,sex,age) in cursor:
    if sex in gender and pronouns:
        print('%s is a %s and %s age is %i.' % (name.capitalize(),
                                                gender[sex],
                                                pronouns[sex],age))

#output : 
# Arta is a Female and her age is 26.
# Sarah is a Female and her age is 40.
# Mehr is a Male and his age is 34.
# Far is a Female and her age is 35.
# Hasan is a Unknown and their age is 12.
cnx.close()
