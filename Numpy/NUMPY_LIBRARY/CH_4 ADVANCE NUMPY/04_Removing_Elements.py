#REMOVING ELEMENTS :-
# IF YOU REMOVE SOME ELEMENTS OR NUMBERS IN THE ARRAY SO YOU CAN USE REMOVE FUNCTION

#EXAMPLE :-

import numpy as np

# BEFORE DELETE
array1 =  np.array([10,20,30,40,50])
print(array1)

# AFTER DELETE
dele = np.delete(array1 , -1 , axis=None)
print(dele)

# TRU=Y WITH 2D ARRAY
array2 = np.array([[10,20],
                   [30,40],
                   [50,60]])

delt = np.delete(array2 , 1 , axis=0)
print(delt)
