import numpy as np

arr = np.arange(1 , 101)
print(arr)

#COMPUTE STATISTICS
mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)
max_val = np.max(arr)
min_val = np.min(arr)

#INDEX OF MIN AND MAXX VALUE
max_idx = np.argmax(arr)
min_idx = np.argmin(arr)

print(f"Mean :- {mean_val}")
print(f"Median :- {median_val}")
print(f"Standard Division :- {std_val}")
print(f"Maximum Element : {max_val}")
print(f"Minimum Element :- {min_val}")
print(f"Maximum {max_val} at index of {max_idx}")
print(f"Minimum {min_val} at index of {min_idx}")