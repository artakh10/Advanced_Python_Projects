'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Jan. 2025
'''

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = 'https://www.motorist.sg/used-cars/toyota?srsltid=AfmBOopCNDez0pAakLB4vnPz1O2aYuWyBvbkfucTyDvbk6VxyRJIBrJJ'
finding_var = 'p'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
#For the name of the car
all_results = soup.find_all(finding_var) 
first_result = all_results[1];first_attrs = first_result.attrs
res_cars_first = soup.find(finding_var, 
                attrs=first_attrs)
res_cars_all = soup.find_all(finding_var, 
                attrs=first_attrs)
print('The first item is: ', res_cars_first.text)
print('The pretty version of the 1st item is: ',
      re.sub(r'\s+',' ',res_cars_first.text).strip()) 

#For the price, paved destination and registration date
#-- 1st way (inefficient):
# price = soup.find_all('div',attrs = {'class':'font-weight-bold price'})
# destination = soup.find_all('div',attrs = {'class':'mileague'})
# date = soup.find_all('div',attrs = {'class':'registration'})
#-- 2nd way: (#select chooses ONLY the specified selection of the word)
destination = soup.select('div[class="mileague"]')
price = soup.select('div[class="font-weight-bold price"]')
date = soup.select('div[class="registration"]')

#For all of them in a DataBase form:
list_res, list_num, list_dest, list_date = [], [], [], []

for j in range(len(price)):
    for lst, text in zip([list_res, list_num, list_dest, list_date], 
                         [res_cars_all[j].text, price[j].text, destination[j].text, date[j].text]):
        lst.append(re.sub(r'\s+', ' ', text).strip())


#To make it into a DataFrame:
df = pd.DataFrame({'Name':list_res,'Price':list_num,
                   'Paved_Destination':list_dest,'Registration_Date':list_date})
df.to_csv('Cars.csv',index=False)