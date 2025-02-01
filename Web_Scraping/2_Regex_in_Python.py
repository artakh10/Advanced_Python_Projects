'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''
import re #importing regex's module
#in re's module we can do: 1) search for a specific regex,
# 2) find a regex (findall), or 3) sub: substitute or change



#Example 1:
str = 'salam arta. salam mehdi. salam susan.'
print(re.search(r'salam',str)) #find salam in "str".
#output : <re.Match object; span=(0, 5), match='salam'>
result = re.search(r'salam',str)
print(result.span()) #output: (0, 5)
print(result.start()) #output: 0 
#start of this expression is from character 0, and ends in character 5
#if there was no salam in my string, output would be 'None'.



#Example 2:
#Now for checking Emails
inp = 'artakhosravi@gmail.com'
em_fin=re.search(r'.*\@.+\..{2,3}',inp)
print(em_fin)
if re.search(r'.*\@.+\..{2,3}',inp) == None:
    print('Not en email')
print(re.findall(r'.*\@.+\..{2,3}',inp)) #print the email basically
#output:['artakhosravi@gmail.com']
print(re.findall(r'^(.*)\@',inp)) #print anything before the @
#output:['artakhosravi']



#Example 3:
#To find the oil price using Regex:
str_oil = 'the price of oil is 65$ for 3 liters'
print(re.findall(r'the price of oil is 65\$ for 3 liters',str_oil) )
#output: ['the price of oil is 65$ for 3 liters']

print(re.findall(r'the price of oil is \d+\$ for \d+ liters',str_oil) )
#output: ['the price of oil is 65$ for 3 liters']
#just checking if they match
result_oil = (re.findall(r'the price of oil is (\d+)\$ for (\d+) liters',str_oil) )
#output: [('65', '3')]
#an array which has 3 tuples
price, liters = result_oil[0]
print(price,liters)

#To make my str more complicated:
str_oil_v2 = '''the price of oil is 65$ for 3 liters for yesterday
the price of oil is 78$ for 3 liters for today
the price of oil is 61$ for 3 liters for 9/4'''
print(str_oil_v2)
result_oil_v2 = (re.findall
                 (r'the price of oil is (\d+)\$ for (\d+) liters for (.*)',
                  str_oil_v2) )

print(result_oil_v2) 
#output: [('65', '3', 'yesterday'), ('78', '3', 'today'), ('61', '3', '9/4')]

#To make it a loop:
for price, liters, day in result_oil_v2:
    print(price,liters, day)
#output : 
# 65 3 yesterday
# 78 3 today
# 61 3 9/4



#Example 4: To use sub:
str = 'salam arta. salam mehdi. Salam parsa. salam susan.'
print(re.sub(r'salam','Hi',str)) #substitute salam with hi.
#output: Hi arta. Hi mehdi. Salam parsa. Hi susan.
#To make it prone to capitalized letters:
print(re.sub(r'[sS]alam','Hi',str)) #[sS] means either s OR S
#output: Hi arta. Hi mehdi. Hi parsa. Hi susan. #yay!
print(re.sub(r'[sS]alam \w+\.','Hi',str))
#means change all the words that come from sala till the end of dot with hi.
#output: Hi Hi Hi Hi
print(re.sub(r'[sS]alam (\w+)\.','Hi \g<1>',str)) #For group finding
#output: Hi arta Hi mehdi Hi parsa Hi susan
#this means this is our first group.
#if i put \g<0> if puts Hi salam arta. Hi salam mehdi. etc.



#Example 5: Coming back to Example 3 for sub example:
str_oil_v2 = '''the price of oil is 65$ for 3 liters for yesterday
the price of oil is 78$ for 3 liters for today
the price of oil is 61$ for 3 liters for 9/4'''
#if we want to make a csv table, we can:
replace_str_oil = 'the price of oil is (\d+)\$ for (\d+) liters for (.*)'
print(re.sub(replace_str_oil,'\g<3>,\g<1>,\g<2>',str_oil_v2))
#it basically prints the groups in the original string-
# -which were specified by the replace_str_oil
#output:
# yesterday,65,3
# today,78,3
# 9/4,61,3