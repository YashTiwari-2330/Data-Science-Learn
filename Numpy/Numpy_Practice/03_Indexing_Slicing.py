import numpy as np

b = np.array([[1,2],[3,4],[5,6]])
print(b[[0,2],[1,0]])

#Boolean indexing (filtering) uses a boolean condition array of the same shape. For instance:

x = np.array([1.0,-1.0,-2.0,3.0])
mask = x < 0
print(mask)

# 1- Given the 2D array below, use slicing to extract the subarray [[6,7],[10,11]]:
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])

print(arr[1:3 , 1:3])

# 2- Using integer-indexing, select elements 1st, 3rd, and 5th from the 1D array np.array([10, 20, 30, 40, 50, 60]).

a = np.array([10,20,30,40,50,60])
index = [0,2,4]
print(a[index])

# 3-Filter the array np.array([5, 12, 7, 3, 8, 15]) to include only values greater than 7.
arr1 = np.array([5,12,7,3,8,15])
filterd = arr1[arr1 > 7]
print(filterd)