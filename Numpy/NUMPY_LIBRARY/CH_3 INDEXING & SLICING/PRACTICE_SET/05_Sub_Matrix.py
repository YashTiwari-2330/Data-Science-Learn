import numpy as np

arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]]
               )

sub_matrix = arr[1:3 , 0:2]
print(f"Sub Matrix is :-\n {sub_matrix}")