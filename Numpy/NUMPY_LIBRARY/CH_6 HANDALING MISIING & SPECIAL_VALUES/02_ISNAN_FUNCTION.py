# ISNAN() :-
# THIS FUNCTION ARE USE TO FIND A MISSING VALUES IN A LARGE AMOUNT OF DATASET,
# IF MISSING VALUES IN DATA HAVE SO OUTPUT GAVE YOU TRUE

import numpy as np

arr = np.array([10,20,np.nan,40,50,np.nan])

nan = np.isnan(arr)

print(nan)

#NOTE :- IS YOU COMPAIR NAN METHOD?
# -> NO WE CAN NOT DIRECTLY COMPAIR A MISSING VALUES