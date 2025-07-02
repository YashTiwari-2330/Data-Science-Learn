# -> IF YOU WORK WITH ARRAY AND IN DATA SCIENCE DATA IS NOT FIXED IT'S CHANGEABLE ,
# -> SO ARRAY IS FIXED SIZE AFTER CREATION YOU DID NOT CHANGE YOU CREATE A NEW ARRAY.
# -> BUT YOU IMPLEMENT A SOME FUNCTION TO PERFORM SOME TASKS.

import numpy as np
# 1ST - INSERT FUNCTION :- WHEN YOU INSERT SOME TASK AT YOUR MANUAL INDEX SO YOU CAN USE A INSERT FUNCTION
#TRY WITH 1D ARRAY

array_1d = np.array([[10,20,30],[40,50,60]])
print(array_1d,type(array_1d))

ins = np.insert(array_1d , 1 , 70 , axis=0)
print(ins)

#TRY WITH 2D ARRAY
array_2d = np.array([[10,20],
                    [30,40],
                    [50,60]])

print(np.insert(array_2d , 3 , [70,80] , axis=0))