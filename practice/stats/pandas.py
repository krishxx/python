# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 06:14:31 2018

@author: Srikrishna.Sadula
"""
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

columns = ['name', 'age', 'gender', 'job']
user1 = pd.DataFrame([['alice', 19, "F", "student"],
['john', 26, "M", "student"]],
columns=columns)
print (user1)

user2 = pd.DataFrame([['eric', 22, "M", "student"],
['paul', 58, "F", "manager"]],
columns=columns)
print (user2)

user3 = pd.DataFrame(dict(name=['peter', 'julie'],
age=[33, 44], gender=['M', 'F'],
job=['engineer', 'scientist']))
print(user3)

type(user1)
p = user1.append(user2)
print (p)
print (user1)
users = pd.concat([user1, user2, user3])
print(users)

user4 = pd.DataFrame(dict(name=['alice', 'john', 'eric', 'julie'],
height=[165, 180, 175, 171]))
print(user4)

merge_inter = pd.merge(users, user4, on="name")
print(merge_inter)

users = pd.merge(users, user4, on="name", how='outer')
print(users)

staked = pd.melt(users, id_vars="name", var_name="variable", value_name="value")
print(staked)

print(staked.pivot(index='name', columns='variable', values='value'))

users # print the first 30 and last 30 rows
type(users) # DataFrame
users.head() # print the first 5 rows
users.tail() # print the last 5 rows
users.index # "the index" (aka "the labels")
users.columns # column names (which is "an index")
users.dtypes # data types of each column
users.shape # number of rows and columns
users.values # underlying numpy array
users.info() # concise summary (includes memory usage as of pandas 0.15.0)

users['gender'] # select one column
type(users['gender']) # Series
users.gender # select one column using the DataFrame
# select multiple columns
users[['age', 'gender']] # select two columns
my_cols = ['age', 'gender'] # or, create a list...
print (my_cols)
users[my_cols] # ...and use that list to select columns
type(users[my_cols])

df = users.copy()
print (df)
df.iloc[0] # first row
df.iloc[0, 0] # first item of first row
df.iloc[0, 0] = 55
users.shape[0]
users.shape[1]
for i in range(users.shape[0]):
    row = df.iloc[i]
    row.age *= 100 # setting a copy, and not the original frame data.
    print (row.age)
print (row)
print(df)

users[users.age < 20] # only show users with age < 20
young_bool = users.age < 20 # or, create a Series of booleans...
print (young_bool)
young = users[young_bool] # ...and use that Series to filter rows
print (young)

users[users.age < 20][['age', 'job']] # select multiple columns
users[(users.age > 20) & (users.gender == 'M')] # use multiple conditions
users[users.job.isin(['student', 'engineer'])][['age','job']] # filter specific values

df = users.copy()
df.age.sort_values() # only works for a Series
df.sort_values(by='age') # sort rows by a specific column
df.sort_values(by='age', ascending=False) # use descending order instead
df.sort_values(by=['job', 'age']) # sort by multiple columns
df.sort_values(by=['job', 'age'], inplace=True) # modify df
print(df)