#NAN_TO_NUM() :-
# ARE USING TO REPLACE A MISSING VALUES INTO OTHER VALUE

import numpy as np

arr = np.array([10,20,30,40,np.nan,60,np.nan])

clean_array = np.nan_to_num(arr , nan=1)

print(clean_array)

#NOTE :-
#-> BY DEFAULT A NAN_TO_NUM FUNCTION ARE USE TO REPLACE A NUN VALUES INTO ZERO
# BUT YOU DO MANUALLY CHANGE A VALUE YOU SHOULD APPLY NAN= ATTRIBUTE IN THE NAN_TO_NUM FUNCTION
