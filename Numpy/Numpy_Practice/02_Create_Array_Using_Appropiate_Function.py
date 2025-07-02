import numpy as np

arr = np.full((3,3),2)
print(arr)


# CREATE ARRANGE FUNCTIONS ARRAY
arr1 = np.arange(0,20 , 2)
print(arr1)

#RESHAPE VALUES
one_d = np.array([1,2,3,4,5,6,7,8,9])
shape = one_d.reshape((3,3))
print(shape)