# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 06:24:50 2018

@author: Srikrishna.Sadula
"""
from __future__ import print_function
import numpy as np

data1 = [1, 2, 3, 4, 5] # list
print (data1)
arr1 = np.array(data1) # 1d array
data2 = [range(1, 5), range(5, 9)] # list of lists
print (data2)
arr2 = np.array(data2) # 2d array
print (arr2)
arr2.tolist() # convert array back to list

np.zeros(10)
np.zeros((3, 6))
np.ones(10)
np.linspace(0, 1, 5) # 0 to 1 (inclusive) with 5 points
np.logspace(0, 3, 4) # 10^0 to 10^3 (inclusive) with 4 points

int_array = np.arange(5)
float_array = int_array.astype(float)

arr1.dtype # float64
arr2.dtype # int32
arr2.ndim # 2
arr2.shape # (2, 4) - axis 0 is rows, axis 1 is columns

arr = np.arange(10, dtype=float).reshape((2, 5))

arr = np.arange(10, dtype=float).reshape((2, 5))
print (arr)
print(arr.shape)
print(arr.reshape(5, 2))


names = np.array(['Bob', 'Joe', 'Will', 'Bob'])
names == 'Bob' # returns a boolean array
names[names != 'Bob'] # logical selection
(names == 'Bob') | (names == 'Will') # keywords "and/or" don't work with boolean
#˓→arrays
names[names != 'Bob'] = 'Joe' # assign based on a logical selection
print (names)
np.unique(names)


nums = np.arange(5)
print (nums)
nums * 10 # multiply each element by 10
nums = np.sqrt(nums) # square root of each element
print (nums)
np.ceil(nums) # also floor, rint (round to nearest int)

np.isnan(nums) # checks for NaN
nums + np.arange(5) # add element-wise
np.maximum(nums, np.array([1, -2, 3, -4, 5])) # compare element-wise
# Compute Euclidean distance between 2 vectors
vec1 = np.random.randn(10)
print (vec1)
vec2 = np.random.randn(10)
print (vec2)
dist = np.sqrt(np.sum((vec1 - vec2) ** 2))
print (dist)
# math and stats
rnd = np.random.randn(4, 2) # random normals in 4x2 array
print (rnd)
rnd.mean()
rnd.std()
rnd.argmin() # index of minimum element
rnd.sum()
rnd.sum(axis=0) # sum of columns
rnd.sum(axis=1) # sum of rows
rnd.mean(axis=0)

data2 = [range(1, 5), range(5, 9)] # list of lists
print (data2)
arr2 = np.array(data2) # 2d array

print (arr2)
arr2[0, :] # row 0: returns 1d array ([1, 2, 3, 4])
arr2[:, 0] # column 0: returns 1d array ([1, 5])
arr2[:, :2] # columns strictly before index 2 (2 first columns)
arr2[:, 2:] # columns after index 2 included
arr3 = arr2[:, 1:4] # columns between index 1 (included) and 4 (excluded)
print(arr3)

arr = np.arange(10, dtype=float).reshape((2, 5))
print (arr)
arr2 = arr[:, [1,2,3]] # return a copy
print(arr2)
arr2[0, 0] = 44
print(arr2)
print(arr)
arr[0,4] = 8
arr2 = arr[arr > 5] # return a copy
print(arr2)
arr2[0] = 44

a = np.array([[ 0, 0, 0],
[10, 10, 10],
[20, 20, 20],
[30, 30, 30]])
b = np.array([[0, 1, 2],
             [3, 4, 5]])
print(a + b)