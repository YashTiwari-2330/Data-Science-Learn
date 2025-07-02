# SHAPE ATTRIBUTE :-
                    # WHEN WORKING WITH MULTIDIMENSIONAL DATA SHAPE HELP YOU TO UNDERSTAND ,
                    # HOW MANY ROWS & COLUMNS IN OUR DATA.

# EXAMPLE :-

import numpy as np

arr_2d = np.array([[1,2,3],
                   [4,5,6]])

print(arr_2d.shape)

#1 - SIZE ATTRIBUTE :-
                # IF YOU HAVE LARGE AMOUNT OF DATA AND YOU DO TO COUNT SO USE SIZE ELEMENT,
                # IT HELP YOU TO COUNT TOTAL ELEMENTS IN ARRAY

#2 - DTYPE ATTRIBUTE :-
                # TYPE ATTRIBUTE USE TO FIND A SIZE OF YOUR ARRAY WHAT TYPE OF NUMERICAL VALUES
                # IN ARRAY.

# EXAMPLE :-

array_2 = np.array([[[1,2,3],
                     [4,5,6],
                     [7,8,9],
                     [10,11,12.12]]])

print(array_2.shape , array_2.size , array_2.dtype)


#3 - ASTYPE ATTRIBUTE :-
                    # IF YOU CHANGE DATA TYPES TO  ANOTHER DATATYPE SO USING THIS ATTRIBUTE

# EXAMPLE :-

arr = np.array([1.2,3.5,4.5,2.8])

print(arr.astype(int))


# - NDIM ATTRIBUTE :-
                    # USING THIS ATTRIBUTE YOU CHECK HOW MANY NUMBER OF DIMENSIONAL ARRAYS

# EXAMPLE :-

array_dimensional = np.array([[[1,2,3],
                     [4,5,6],
                     [7,8,9],
                     [10,11,12.12]]])

print(array_dimensional.ndim)
