from os import remove

import numpy as np

arr = np.array([10,20,30,40,50])
arr[arr > 25] = 1
print(arr)

# REVERSE ARRAY USING SLICING
print(arr[::-1])