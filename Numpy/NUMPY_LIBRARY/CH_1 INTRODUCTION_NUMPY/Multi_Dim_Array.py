# MULTI-DIMENSIONAL ARRAY ;-

# THERE ARE MULTIPLE LAYERS OF DATA IN SINGLE VARIABLE

# MULTI-DIMENSIONAL ARRAY IS ALSO 1D,2D ARRAYS OF MIXER


# WHAT AND HOW TO CREATE MATRIX IN USING NUMPY ?

# A MATRIX CALLED A DIFFERENT TYPE OF MATHEMATICS FUNCTION PERFORM IN ARRAYS

# CREATE MATRIX USING NUMPY , EXAMPLE

import numpy as np
from numpy.matrixlib.defmatrix import matrix

# CREATE MATRIX ARRAYS
ma = np.matrix([[25,30,52],
                [23,63,98],
                [85,69,25]])

ba = np.matrix([[30,22,40],
                [25,63,59],
                [32,63,25]])

ca = np.array(ma + ba)

print(ca , type(ca))


# CONVERT LIST INTO NUMPY ARRAYS

L1 = [25,69,96,58]
print(L1 , type(L1))

print(np.array(L1))