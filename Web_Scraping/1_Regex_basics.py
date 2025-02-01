'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''
'''
Q: If there was a random website, how can I write a Python Script that  can take
specific information out of it and use it for its own?
E.g.: A website includes automobile expenses. I want to write a code that will
read the expenses and tell me the price of the car I want.
In other words, I want it to read from web/API/etc. the information I want,
and then analyze the output. : this is called Network access.
Our work here is called WEB SCRAPING.
'''
'''
Regex is basically Regular Expression.
Q: How is Regex involved?
A: Regex is like talking to computers and telling them what I want, which part I want.
E.g.: If I say my name is Amir Hossein Sadramini, it is clear that the first name is Amir-Hossein, and
Last name is Sadramini. This identification is done by Regex.

I am using https://regex101.com/ for online analyzing.
'''
'''
IMPORTANT REGEX SYNTAX:
Important: Put the "Flavor" as Python.4
".": Means anything
\d : digit
\w : word (all alphabets and _)
\s : white-space (Tab, space, enter, etc.)
* : however many (from zero to infinity)
+ : from 1 to infinity
a + : minimum 'a'.
a* : it doesn't matter if it didnt include "a".
\. : the "dot", not the "anything" definition.
[ab]: either "a" or "b".
(): capturing group or grouping something.
{n,m}: minimum n and maximum m.
a{4}: exactly 4 a's.
a{4,8}: between 4 to 8 a's.
.{1,3}: anything between 1 to 3.
[^abc]: anything except a, b and c. ([^] here means we reversed it.)
^: start of the line.
$: end of the line.
.*$: whatever we have, consider all of them till the end of its line.
^\d: start of the line with a digit.
[^\d]: start of the line be with anything but a digit.
'''
'''
E.g. : Emails:
@.* : find @ and whatever else is after it.
@.*\. : find wherever @ is present, show it to me till you see a dot.
@(.*)\. : CAPTURING GROUP: whatever is after @ before dot is of my concern.
My groups will be : yahoo, gmail, hotmail, etc.

E.g.: Phone number:
^phone:(\d{11})$: the line starts with "phone:",-
-I want whatever after it starts with digits,-
-and continue for 11 digits and keep it till the end of the line.
'''
'''
Greedy Regex: We want lazy Regex, therefore we'll use a "?". ? = lazy sign

E.g.: We have an html code.
<html>
<body>
Line line line.
</body>
</html>
\<.*?>: if you found a "<", don't be greedy and take
whatever comes after that till ">", if you got to ">", say you found it.

E.g.: if my line is this:
this is the end first this line end. and this is the. second line end 
when i put : "this .*? end"
output will be 3 matches:
this is the end // this line end // this is the. second line end 

E.g.: Separating names:
If the code is: ^(\w*)\.*(\w*)\.+(\w+.)
output will be:
Arta//.//Familyname
Art//.//Second//.//Name
a//.//arta//.//artiston
a//.//middle//.//last
'''