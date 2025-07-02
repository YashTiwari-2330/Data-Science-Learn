import numpy as np

#1D ARRAY INDEXING
arr = np.array([10,20,30,40,50,47])
print(arr[0])
print(arr[3])
print(arr[-4])

# * FANCY INDEXING :-CHOSE A MULTIPLE ELEMENTS USING INDEXING
# A FANCY INDEXING DEFINE AS ONLY LIST FOM

# EXAMPLE :-
print(arr[[0,2,3]])

# BOOLEAN INDEXING :-
# A BOOLEAN INDEXING ARE PERFORM A CONDITION
# YOU WILL PASS CONDITION AND TAKE OUTPUT AS PER YOUR CONDITION
print(arr[arr % 2 == 0])

#--------------------------------------------------------------------------------------------#

#2D ARRAY INDEXING :- 1ST DEFINE AS COLUM AND 2ND DEFINE AS ROWS
arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]]
                  )

print(arr_2d[1,2])

# NEGATIVE INDEXING :- AN NEGATIVE INDEXING CAN NOT START WITH ZERO IT IS START WITH 1 INDEX

print(arr_2d[-3,-2])


