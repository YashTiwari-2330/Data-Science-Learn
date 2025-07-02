# WHAT IS RESHAPING ?
#-> WITHOUT MODIFY A DATA YOU CAN CHANGE A SHAPE OF ARRAY.
#-> IF DIEMANSION ARE MATCH THAN YOU RESHAPE A DATA

# SYNTAX :- reshape() 1D ARRAY INTO 2D ARRAY
import numpy as np

arr_shap = np.array([10,20,30,40,50,60])

print(arr_shap.reshape(2,-1))

# 2D ARRAY INTO 3D ARRAY
reshapped = arr_shap.reshape(1,2,3)
print(reshapped)

#2- FLATTING AND REVAL :-
# IF YOU CONVERT 2D AND MULTIDIMENSIONAL ARRAY INTO 1D ARRAY SO USE THIS,
# FLATTING METHOD RETURN COPY ARRAY THEY DO NOT MODIFY REAL ARRAY

#3- REVAL :- IT RETURN VIEW IF POSSIBLE.
# REVAL METHOD CAN MODIFY CURRENT ARRAY

arr_2 = np.array([[10,20,30],
                  [40,50,60]])

flat = arr_2.flatten()
print(flat)
reval = flat.ravel()
print(reval)
