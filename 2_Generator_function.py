'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''

'''
Sometimes I want to call a function for a large amount of data,
or call it unlimited times, etc.
For these evenets, we use generators.
In generators, we have "yield", unlike normal functions that have return.
Unlike return that throws the answ away, yield keeps it in the memory.
We use generator functions for for and while loops.
'''
#Normal function:
def firstn():
    return (1,2,3)
print(firstn()) #output: (1,2,3) no matter what.

#Function using yield instead of return.
def firstn():
    yield 1
    yield 2
    yield 3
print(firstn()) #output: <generator object firstn at 0x000001F9F3045B30>

#Using generators in a for loop:
for i in firstn():
    print(i) #output: 1 /n 2 /n 3
    #because it remembred what the function had kept inside
    #and since it is in a loop, it returns i as the items in the function.
    #this doesn't take up space or memory
    #if i used a loop such as for i in (1,2,3); it takes up memory
    #and takes a long time to run.

#Example: Make a function that returns the 0 to n numbers
def firstn(n):
    num = 0 #initially my number is zero
    while (num < n): #as long as my number is less than zero,
        yield num #yield (grab) the number
        num +=1 #and then add one to it.
for i in firstn(10):
    print(i) #output : 0,1,2,3,4,5,6,7,8,9