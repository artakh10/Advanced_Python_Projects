'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''
'''
Our databases are similar to a huge excel file with columns, rows and fields.
Very matrice like. these are the classic SQL databases.
BUT! If I want to establish a huge sales website,
I will have to make a database for i.g., the goods' name, color, ram size, hard size, etc.
E.g. I have a Lenovo laptop that is blue, has 8 GB ram and 500 GB hard.
But if someone says hey, I have a doll I want to sell, then this databse won't work efficienctly anymore.
Thus, I have to add two other columns such as model and weight.
Now if someone says I have a book I want to sell, then those columns won't work for it either.
So, we need a more efficient database. Here's where NoSQL comes in.
'''
'''
NoSQL is efficient for its ability to handle multiple database types,
is agile, and has the ability for very large scales.
Agile: توسعه سریع
Scale:  تا تعداد زیاد بتونه ساپورت کنه
'''
'''
Database types: 
I) Document Store: saves multiple goods with different columns.
It's as if I'm storing multiple documents. I am not specifying the fields.
II) Graph Databases: For social media
III) Key value stores: Like Python dictionaries: A:B & C:D
IV) Wild Column: Cassandra and Redis and Hpace
MongoDB: Dynamic Schema
* For connecting Python and Mongo, we can use the pymono package.
'''
''''''''''''''''''''''''''''''''''''''''''
