#  What is Aggregation in NumPy?
# Aggregation functions perform summary statistics on arrays ,
# — such as sum, min, max, mean, median, etc.

import numpy as np
from numpy.ma.core import minimum

arr = np.array([10,20,30,40,50,60])

# 1- SUM() FUNCTION - SUM OF ALL ELEMENTS

arr0 = np.sum(arr)
print(arr0)

# 2- PROD() - FIND PRODUCT OF All elements
arr_1 = np.array([10,20,30,40,50])
prod = np.prod(arr_1)
print(prod)

# 3- MEAN() - FIND AVERAGE (MEAN) OF GIVEN DATA
mean = np.mean(arr_1)
print(mean)

# 4- STD() :- FIND STANDARD DEVIATION
std = np.std(arr_1)
print(std)

# 5- VAR() :- FIND VARIANCE
var = np.var(arr_1)
print(var)

# 6- MIN() , MAX() :- IN ARRAY FIND MINIMUM AND MAXIMUM ELEMENTS IN ARRAY
mini = np.min(arr_1)
print(mini)
maxi = np.max(arr_1)
print(maxi)

# 7- ARGMIN() AND ARGMAX() :- FIND A INDEX OF MIN AND MAX ARGUMENTS IN ARRAY
arg_min = np.argmin(arr)
print(arg_min)
arg_max = np.argmax(arr_1)
print(arg_max)

# 8- MEDIAN() :- FIND MEDIAN VALUES IN ARRAY
mid = np.median(arr)
print(mid)

# 9 - PERCENTILE() - PERCENTILE VALUES
percent = np.percentile(arr_1 , 25)
print(percent)

# 10 - PTP()-PEAK-TO-PEAK :- FIND MAX - MIN VALUES
max_mix = np.ptp(arr_1)
print(max_mix)

# 11- CUMSUM() :- CUMULATIVE SUM ADDING A SUM OF AHEAD NUMBERS
cum = np.cumsum(arr)
print(cum)

# 12- CUMPROD() :- CUMULATIVE PRODUCT GET ADD ALL ELEMENTS PRODUCT OF NUMBERS
cumprod = np.cumprod(arr)
print(cumprod)