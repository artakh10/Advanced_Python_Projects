'''
Specifically for the Advanced Python Programming Course
Author: Arta Khosravi
Last Update: Feb. 2025
'''
'''
I used this dataset from Kaggle for analyzing and training:
https://www.kaggle.com/datasets/sudalairajkumar/novel-corona-virus-2019-dataset
'''
'''
Decision Tree can be a good choice as I want to do classification.
'''

import csv
from sklearn import tree

x = []  # input
y = []  # output
path = r'C:\Users\Asus\Advanced_Python\ML_basics\covid_19_data.csv'
# Use raw string for the file path
with open(path, 'r') as csvfile:
    data = csv.reader(csvfile)  # consider the csv file
    for line in data:
        x.append(line[4:6])  # put Province/State, Country/Region, Confirmed, Deaths as inputs
        y.append(line[6])     # put Recovered as output
    # print(x[1]) #output: [Confirmed:'1',Deaths: '0']
    # print(y[1]) #output: Recovered: 0
x = x[1:10000]; y=y[1:10000] 
#removing the first row that are the names (string) 
# and keeping the first 100000 data since the file is too long.
clf = tree.DecisionTreeClassifier() #considering the decision tree classifier as my classification method
clf = clf.fit(x, y) #fit x and y: choose a classification method and fit the data on it.
new_data = [[100,0],[200,100],[10,0],[12,0],
            [1,1],[150000,138],[1e+8,1905]] 
            #random new data to see if the prediction model works
answer = clf.predict(new_data) #predicting the recovered data of the new_data
#output: ['0' '4' '0' '0' '0' '9211' '11881']
print(answer)