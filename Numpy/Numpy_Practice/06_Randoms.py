import numpy as np

# rng = np.random.default_rng(42)
# print(rng)
#
# rand_vals = rng.random(5)
# print(rand_vals)
#
# ints = rng.integers(0 , 100 , 5)
# print(ints)
#
# norms = rng.standard_normal(3)
# print(norms)

#1- Generate a 2×3 array of random floats between 0 and 1.
rng = np.random.default_rng(0)
arr = rng.random((2,3))
print(arr)

#2- Generate 5 random integers between 1 and 100 (inclusive) with a fixed seed for reproducibility.
rng1 = np.random.default_rng(213)
integer = rng1.integers(1,101,5)
print(integer)

#3-
rg = np.random.default_rng()
sample = rng.standard_normal(1000)
print("Empirial Mean :-" , np.mean(sample))
print("Emperial Std :-" , np.std(sample))