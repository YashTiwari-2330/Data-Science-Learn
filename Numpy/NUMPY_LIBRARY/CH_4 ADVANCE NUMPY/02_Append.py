# APPEND FUNCTION :-
    # -> AN APPEND FUNCTION WILL USE TO ADD SOME ITEMS AT THE END OF ELEMENTS

import numpy as np
#TRY WITH 1D ARRAY

array_1d = np.array([10,20,30,40,50])
print(array_1d)

app = np.append(array_1d , 60)
print(app)

#TRY WITH 2D ARRAY

array_2d = np.array([[10,20],
                     [30,40],
                     [50,60]])
print(array_2d)

app2 = np.append(array_2d , [[70,80]] , axis=0)
print(app2)