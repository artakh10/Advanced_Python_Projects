'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''

'''
Lambda functions: unlike normal def functions, they are anonymous.
As in they are usable once. They use a defined arguement (x,y,etc.) and
an expression.
'''
# 1) Example of using a lambda function
my_func = lambda x: x * 2
print(my_func(3))

# 2) Example of using a lambda function in lists
#-- I) Sorting a list
list_one = [(3,4),(7,1),(5,9),(2,2)]
list_one.sort()
print(list_one) #sorted based on first array

#-- II) Sorted based on the second array using lambda
list_one = [(3,4),(7,1),(5,9),(2,2)]
list_one.sort(key = lambda x: x[1]) 
print(list_one)

'''
Map / filter / (reduce (not important))
Map: If we have a list of different stuff, map says to apply a function
to all the stuff.
Filter: It says we have a list, filter it based on what I'm saying (function).
'''

#-- 1) Map Example: wanting to x2 all my list items.
list_map = [1,3,4,2,0.5]
outp_map = (map(lambda x: x*2,list_map)) #mapping my function to my list above
print(outp_map)
#output : <map object at 0x00000193B8B87520>
print(list(outp_map))
#output : [2, 6, 8, 4, 1.0]

#-- 2) Map Example: Call numbers a string
#-- USING CONDITIONS IN LAMBDA:
numbers = [10,11,8,7,100,7,9,21]
#I want to call numbers > 10 big, and <10 small.
numbers_map = map(lambda x: 'big' if x > 10 else 'small',numbers)
print(numbers_map) #output : <map object at 0x0000026DD39418E0>
print(list(numbers_map))
#output : ['small', 'big', 'small', 'small', 'big', 'small', 'small', 'big']

#-- 3) Filter Example:
list_filter = [1,3,4,2,0.5]
outp_filt_list = list(filter(lambda x: x % 2 == 0,list_filter)) #Only give me the odd numbers.
print(outp_filt_list) #output : [4, 2] (if True: gives answ)