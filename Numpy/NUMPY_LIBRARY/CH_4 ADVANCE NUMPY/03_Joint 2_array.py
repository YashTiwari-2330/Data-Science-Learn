# IF YOU JOINT MORE THAN 2 ARRAY SO YOU CAN USE A CONCATENATE FUNCTION
# THIS FUNCTION ARE JOINT TWO AND MORE DIFFERENT ARRAY AT ONCE.

import numpy as np

#1D ARRAY

arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])

joint = np.concatenate([[(arr1 , arr2)]])
print(joint , np.ndim(joint))