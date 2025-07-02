#STAKING ARRAY :-
# IF YOU COMBINE A MORE THAN 1 ARRAY WITH VERTICALLY AND HORIZONTALLY

#THEY GAVE A FUNCTION TO CONVERT YOUR ARRAY AS YOU WISH

#VSTAKE -> CREATE ARRAY AS ROW WISE
#HSTAKE -> CREATE ARRAY AS COLUM WISE

import numpy as np

arr1 = np.array([{
    "name" : "Yash",
    "Age" : 20
}])

arr2 = np.array([{
    "name" : "Ajay",
    "Age" : 22
}])

# ARRAY COMBINE AT VERTICALLY STAKE FOM
print(np.vstack((arr1 , arr2)))

# ARRAY COMBINE AT HORIZONTALLY STAKE FOM
print(np.hstack(((arr1 , arr2))))


#=====================================================================================#

# WHAT IS SPLIT ?
#-> AN MAIN ARRAY HAS DEVIDE INTO MULTIPLE SUB ARRAYS , CONVERT INTO SMALL PARTS

#EXAMPLE :-
arra = np.array([10,20,30,40,50,60])

print(np.split(arra , 6))

arra2 = np.array([[10],[20],[30],[40]])

print(np.vsplit(arra2 , 4))

print(np.hsplit(arra2 , 1))