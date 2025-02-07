'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Feb. 2025
'''

from sklearn import tree
import pandas as pd
from random import randint as rd

list_model=[];brand_name=[]
path = r'C:\Users\Asus\Advanced_Python\fetch_data.csv'
df = pd.read_csv('fetch_data.csv')

brand_num = pd.factorize(df['Brand'])[0]
brands_dict = dict(zip(brand_num,df['Brand']))

df['Brand_num'] = brand_num
features =['Brand_num',	'Lineage','Day','Month','Year']
x = df[features];y = df['Price']
clf = tree.DecisionTreeClassifier().fit(x, y)


new_dat_2 = [[rd(min(brand_num),max(brand_num)),120,rd(1,31),rd(1,12),2100],
 [rd(min(brand_num),max(brand_num)),25000,rd(1,31),rd(1,12),1998]
 ]
answer = clf.predict(new_dat_2) 
print(answer)
#random output: ['$119,988' '$97,988']
# tree.plot_tree(clf)

#Pretty formatting:
for i, data in enumerate(new_dat_2):
    for key in brands_dict:
        brand_num, lineage, day, month, year = data
        price = answer[i]
        if key == brand_num:
            print("For the Brand",str(brands_dict[key]), 
                    "(Brand Number: "+str(brand_num)+")"+',', 
                    "Lineage",str(lineage)+',',
                    "and the date being", 
                    str(day)+'/'+str(month)+'/'+str(year),
                    "the predicted price is", str(price)+'.')
