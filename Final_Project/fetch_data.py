'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Feb. 2025
'''
#Required packages
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
#Pay attention that if the specified website includes javascript,- 
# -Selenium must be used.

#Base url and its continuity for the further pages
url = 'https://www.motorist.sg/used-cars'
params = {'srsltid': 'AfmBOopCNDez0pAakLB4vnPz1O2aYuWyBvbkfucTyDvbk6VxyRJIBrJJ'}
list_name, list_num, list_dest, list_date = [], [], [], []
list_day=[];list_month=[];list_year=[]

# url = 'https://www.motorist.sg/used-cars?srsltid=AfmBOopCNDez0pAakLB4vnPz1O2aYuWyBvbkfucTyDvbk6VxyRJIBrJJ'

for page in range(1, 10):  #Scraped data from the first ten pages
    params['page'] = page  
    response = requests.get(url, params=params)
    # response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    name = soup.select('div[class="make-model"]')
    destination = soup.select('div[class="mileague"]')
    price = soup.select('div[class="font-weight-bold price"]')
    date = soup.select('div[class="registration"]')

    #For all of them in a DataBase form:

    for j in range(len(price)):
        for lst, text in zip([list_name, list_num], 
                            [name[j].text, price[j].text, 
                            ]):
            lst.append(re.sub(r'\s+', ' ', text).strip())
        #Remove the "," and "km" from the leneage data:
        list_dest.append(re.sub(r'[^\d]', '', destination[j].text).strip())
        #To only keep the dates of the submited year:
        match_date = re.search(r"(\d{2}/\d{2}/\d{4})\s*\((.*)\)", 
                               date[j].text)
        if match_date:
            list_date.append(re.sub(r'\s+', '', 
                                    match_date.group(1)).strip())
        #To separate the day, month and year from one another:
        match_day = re.search(r"(\d{2})/(\d{2})/(\d{4})", date[j].text
                               )
        if match_day:
            list_day.append(re.sub(r'\s+', '', 
                                    match_day.group(1)).strip())
            list_month.append(re.sub(r'\s+', '', 
                                    match_day.group(2)).strip())
            list_year.append(re.sub(r'\s+', '', 
                                    match_day.group(3)).strip())
#To make it into a DataFrame:
df = pd.DataFrame({'Name':list_name,
                   'Lineage':list_dest,
                   'Registration_Date':list_date,
                   'Day':list_day,'Month':list_month,'Year':list_year,
                   'Price':list_num})

list_name_brand=[];list_name_model=[]
for name in df['Name']: #To separate the name into model and brand
    match_name = re.search(r"^(\w+)\s+(.*)", name)
    if match_name:
        list_name_brand.append(match_name.group(1))
        list_name_model.append(match_name.group(2))  

df['Brand'] = list_name_brand;df['Model'] = list_name_model
pd.set_option('display.max_columns', None)
df = df.drop_duplicates()
print(df.head(5))

df.to_csv('fetch_data.csv',index=False)