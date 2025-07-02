import numpy as np

# EACH ROW IS A SUBJECT'S MARKS AND COLUM IS A STUDENTS

marks = np.array([
    [85, 78, 92, 88],  # Student 1
    [76, 85, 80, 90],  # Student 2
    [90, 92, 88, 94],  # Student 3
    [70, 75, 72, 68],  # Student 4
    [88, 89, 84, 86]   # Student 5
])

# 1ST UNDERSTANDING A SHAPE OF ARRAY
print(f"Shape :- {np.shape(marks)}")

# 2nd  Total Marks Of Each Student's
print(f"Total Marks :- {np.sum(marks , axis=1)}")

# 3rd AVERAGE MARKS OF PER STUDENTS
print(f"Average Marks :- {np.mean(marks , axis=1)}")

#4th TOTAL AND AVERAGE PER STUDENT
print(f"Subject Total :- {np.sum(marks , axis=0)}")
print(f"Average of Subject :- {np.mean(marks , axis=0)}")

# 5th MIN , MAX ,MARKS IN EACH SUBJECT
print(f"Minimum per subject :- {np.min(marks , axis=0)}")
print(f"Maximum Per Subject :- {np.max(marks , axis=0)}")

#6th FIND THE BEST AND WEAKEST STUDENT
print(f"Best Student :- {np.argmax(marks , axis=1)+1}")
print(f"Worst Student :- {np.argmin(marks , axis=1)+1}")

#7th CUMULATIVE MARKS ANALYSIS
print(f"Cumulative Marks Row-Wise : \n {np.cumsum(marks , axis=1)}")


#8th VARIANCE AND STANDARD DECISION OF SUBJECT
print(f"Standard Deviation Per Subject :- {np.std(marks , axis=0)}")
print(f"Variance Per Subject :- {np.var(marks , axis=0)}")

#9th PERCENTILE ANALYSIS
print(f"Percentile :- {np.percentile(marks , [25,50,75] ,  axis=0)}")