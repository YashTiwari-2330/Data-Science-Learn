import time

import numpy as np
from openpyxl.styles.builtins import total

# 1- Given a = np.array([1,2,3]) and b = 10, use broadcasting to add 10 to every element of a.
a = np.array([10,20,30])
print(a + 10)

# 2- Let X = np.arange(1,7).reshape((2,3)) and y = np.array([1,2,3]). Compute X + y and explain the result.
x = np.arange(1 , 7).reshape((2,3))
print(x)
y = np.array([1,2,3])
print(x+y)

# 3- Compare the performance of summing a large array with a Python loop vs. using np.sum(). (Hint: time each method with a large array.)
arr = np.random.rand(10000000)
start = time.time()
tot = 0

for val in arr:
    tot += val
    print("Lopp Time :-" , time.time() - start)
    break

start = time.time()
total2 = np.sum(arr)
print("Numpy Sum Time :-",time.time()-start)

