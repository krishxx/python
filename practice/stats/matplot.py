# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 06:29:27 2018

@author: Srikrishna.Sadula
"""

import numpy as np
import matplotlib.pyplot as plt
#seaborn
#%matplotlib inline
x = np.linspace(0, 10, 50)
print (x)
sinus = np.sin(x)
print (sinus)
plt.plot(x, sinus)
plt.show()

plt.plot(x, sinus, "o")
plt.show()

cosinus = np.cos(x)
plt.plot(x, sinus, "-b", x, sinus, "ob", x, cosinus, "-r", x, cosinus, "or")
plt.xlabel('this is x!')
plt.ylabel('this is y!')
plt.title('My First Plot')
plt.show()

import pandas as pd
import seaborn as sns

try:
    salary = pd.read_csv("../data/salary_table.csv")
except:
    url = 'https://raw.github.com/duchesnay/pylearn-doc/master/data/salary_table.csv'
    salary = pd.read_csv(url)
df = salary
colors = colors_edu = {'Bachelor':'r', 'Master':'g', 'Ph.D':'b'}
plt.scatter(df['experience'], df['salary'], c=df['education'].apply(lambda x:colors[x]), s=100)

# Set up the matplotlib figure: 3 x 1 axis
f, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)
i = 0
for edu, d in salary.groupby(['education']):
    sns.distplot(d.salary[d.management == "Y"], color="b", bins=10, label="Manager", ax=axes[i])
    sns.distplot(d.salary[d.management == "N"], color="r", bins=10, label="Employee", ax=axes[i])
    axes[i].set_title(edu)
    axes[i].set_ylabel('Density')
    i += 1
plt.legend()


sns.pairplot(salary)
plt.show()

g = sns.PairGrid(salary, hue="management")
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
g.add_legend()