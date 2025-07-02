#isinf():-
# THIS FUNCTION ARE CHECK A VALUES IN ARRAY A NUMBERS ARE INFINITE OR NOT.
# IF INFINITE VALUES ARE EXIST SO RETURN A BOOLEAN VALUES LIKE TRUE AND FALSE

import numpy as np

arr = np.array([10,20,30,np.inf , 4 , -np.inf])

print(np.isinf(arr))

clean = np.nan_to_num(arr , posinf=1000 , neginf=-1000)
print(clean)