'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''
'''
Web scraping is bascially scraping data from the web.
Sometimes in a specific network, one can request and see the data directly.
E.g.: I have arta.net, I read it from web, with Regex I get all its link,
since it's all html links, I drop all the links in a database and verify
whether they've been checked or not, and the second time I run it all the
links will be read and all the checks will be verified and unrepeated links
will be dropped in the database again, and in the end we'll reach google.
'''
import requests
#API: Application Programming Interface
# res = requests.get('https://google.com') #our whatever else API


#Example 1:
res = requests.get('https://api.github.com/')
print(res) #output: <Response [200]> #because it's an http code. #200 means OK
# This way I can read data from the web.
print(res.text) #output: JSON output: similar to Python's dictionary
print(res.json) #output: <bound method Response.json of <Response [200]>>
link = res.json()
print(link['user_url']) #output: https://api.github.com/users/{user}



#Example 2:
response = requests.get('https://www.amazon.sg/s?k=amazon+laptop&adgrpid=94734167726&hvadid=584074514612&hvdev=c&hvlocint=9062538&hvlocphy=2364&hvnetw=g&hvqmt=e&hvrand=16019984847815445556&hvtargid=kwd-353766051967&hydadcr=8964_328101&mcid=7ad5f9b5f34134f1821b1f3801d56011&qid=1738306489&rnid=10510243051&tag=googlepcstdsg-22&ref=sr_nr_p_36_0_0&low-price=15&high-price=350')
# print(response.text)
'''
Beautiful Soup Module can do what Regex does in a simplified way.
As in it will separate parts of a file in different formats.
'''
from bs4 import BeautifulSoup
# soup = BeautifulSoup(page,'how') #the how here in api is html pages
soup = BeautifulSoup(response.text,'html.parser')
value = soup.find('h2') #find the first text that has 'h2' in it.
result = soup.find_all('h2') #find all the texts with 'h2' in them.
result_1 = result[2]
print(result_1.attrs) #output: {'class': ['a-size-base', 'a-spacing-small', 'a-spacing-top-small', 'a-text-normal']}
res_laptop = soup.find('h2', 
                attrs={'a-size-base', 'a-spacing-small', 
                       'a-spacing-top-small', 'a-text-normal'})
# print(res_laptop.text)
#To make it more pretty:
import re
print(re.sub(r'\s+',' ',res_laptop.text).strip()) #strip() deletes the unnecessary spaces from the start and finish of the line.
all_vals = soup.find_all('h2', 
                attrs={'a-size-base', 'a-spacing-small', 
                       'a-spacing-top-small', 'a-text-normal'})
for lp in all_vals:
    print(re.sub(r'\s+',' ', lp.text).strip()) #gives all the laptop names and their qualities of the first page