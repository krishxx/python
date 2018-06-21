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
print (df)
df.age.sort_values() # only works for a Series
df.sort_values(by='age') # sort rows by a specific column
df.sort_values(by='age', ascending=False) # use descending order instead
df.sort_values(by=['job', 'age']) # sort by multiple columns
print (df)
df.sort_values(by=['job', 'age'], inplace=True) # modify df
print(df)

print(df.describe())

print(df.describe(include='all'))
print(df.describe(include=['object'])) # limit to one (or more) types

print(df.groupby("job").mean())

for grp, data in df.groupby("job"):
    print(grp, data)
    
df = users.append(df.iloc[0], ignore_index=True)
print(df.duplicated()) # Series of booleans
# (True if a row is identical to a previous row)
df.duplicated().sum() # count of duplicates
df[df.duplicated()] # only show duplicates
df.age.duplicated() # check a single column for duplicates
df.duplicated(['age', 'gender']).sum() # specify columns for finding duplicates
df = df.drop_duplicates() # drop duplicate rows

# Missing values are often just excluded
df = users.copy()
df.describe(include='all') # excludes missing values
# find missing values in a Series
df.height.isnull() # True if NaN, False otherwise
df.height.notnull() # False if NaN, True otherwise
df[df.height.notnull()] # only show rows where age is not NaN
df.height.isnull().sum() # count the missing values
# find missing values in a DataFrame
df.isnull() # DataFrame of booleans
df.isnull().sum() # calculate the sum of each column

df.dropna() # drop a row if ANY values are missing
df.dropna(how='all') # drop a row only if ALL values are missing

df.height.mean()
df = users.copy()
df.loc[df.height.isnull(), "height"] = df["height"].mean()
print(df)

df = users.copy()
print(df.columns)
df.columns = ['age', 'genre', 'travail', 'nom', 'taille']
df.travail = df.travail.map({ 'student':'etudiant', 'manager':'manager',
'engineer':'ingenieur', 'scientist':'scientific'})
assert df.travail.isnull().sum() == 0
df['travail'].str.contains("etu|inge")

size = pd.Series(np.random.normal(loc=175, size=20, scale=10))
# Corrupt the first 3 measures
size[:3] += 500

size_outlr_mean = size.copy()
size_outlr_mean[((size - size.mean()).abs() > 3 * size.std())] = size.mean()
print(size_outlr_mean.mean())

import tempfile, os.path

tmpdir = tempfile.gettempdir()
print (tmpdir)

csv_filename = os.path.join(tmpdir, "users.csv")
users.to_csv(csv_filename, index=False)
other = pd.read_csv(csv_filename)

print (other)

xls_filename = os.path.join(tmpdir, "users.xlsx")
users.to_excel(xls_filename, sheet_name='users', index=False)
pd.read_excel(xls_filename, sheetname='users')
# Multiple sheets
with pd.ExcelWriter(xls_filename) as writer:
    users.to_excel(writer, sheet_name='users', index=False)
    df.to_excel(writer, sheet_name='salary', index=False)
    
pd.read_excel(xls_filename, sheetname='users')
pd.read_excel(xls_filename, sheetname='salary')

import pandas as pd
import sqlite3
db_filename = os.path.join(tmpdir, "users.db")

conn = sqlite3.connect(db_filename)

url = 'https://raw.github.com/neurospin/pystatsml/master/data/salary_table.csv'
salary = pd.read_csv(url)
salary.to_sql("salary", conn, if_exists="replace")

cur = conn.cursor()
values = (100, 14000, 5, 'Bachelor', 'N')
cur.execute("insert into salary values (?, ?, ?, ?, ?)", values)
conn.commit()

salary_sql = pd.read_sql_query("select * from salary;", conn)
print(salary_sql.head())
pd.read_sql_query("select * from salary;", conn).tail()
pd.read_sql_query('select * from salary where salary>25000;', conn)
pd.read_sql_query('select * from salary where experience=16;', conn)
pd.read_sql_query('select * from salary where education="Master";', conn)