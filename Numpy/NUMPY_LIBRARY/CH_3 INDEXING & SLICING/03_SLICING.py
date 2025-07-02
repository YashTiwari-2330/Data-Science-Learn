import numpy as np

# 1D ARRAY SLICING [start:stop:step]
arr = np.array([10,20,30,40,50])
print(arr[1:4])
print(arr[0:4])
print(arr[:4])
print(arr[0:])
print(arr[:: -1])
print(arr[::2])             # INCREMENT BY 2

#2D ARRAY SLICING
arr_2d = np.array([[10,20,30],
                   [40,50,60],
                   [70,80,90]]
                  )
print(arr_2d[0:2 , 1:2])