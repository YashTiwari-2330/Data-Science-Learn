import numpy as np

arr = np.array([2,8,4,10,6])

print("Mean :-" , np.mean(arr))
print("Median :-" , np.median(arr))
print("Std :-" , np.std(arr))


# 2- Given a 2D array M = np.array([[1,2,3],[4,5,6]]), compute the sum of each column and the sum of each row.

M = np.array([[1,2,3],
              [4,5,6]])

col_sum = np.sum(M , axis=0)
row_sum = np.sum(M, axis=1)
print("Colum_Sum :-" , col_sum)
print("Row_Sum :-" , row_sum)
print("Sum is :-" , np.sum(M))

# 3- Given an array of numbers, use NumPy to find the 25th and 75th percentiles.
data = np.array([10,20,30,40,50])
p25 = np.percentile(data , 25)
p75 = np.percentile(data , 75)

print(f"25th Percentile :- {p25}")
print(f"26th percentile :- {p75}")