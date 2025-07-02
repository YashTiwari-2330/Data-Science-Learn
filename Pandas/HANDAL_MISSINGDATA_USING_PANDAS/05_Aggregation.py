# AGGREGATION INVOLVE TO PERFORM SUMMARY STATISTIC.

# WHAT IS SUMMARY STATISTIC?
# -> PROVIDE A NUMERICAL TASK

# GroupBy + Aggregation
# Example

#COMMON AGGREGATION FUNCTION LIKE..

#1. SUM() :- Return sum values of columns

import pandas as pd

data = {
    "Name": ['Yash', 'Ajay', 'Vijay', 'Akash'],
    "Age": [25, 32, 45, 21],
    "Salary": [10000, 250000, 21000, 80000]
}

df= pd.DataFrame(data)

print(df.sum(),print(" "))

# GroupBy + Aggregation
# Example
#2. MEAN() :- Calculate the average of values

avg_salary = df.groupby("Name")["Salary"].mean()
print("Mean Of average Salary :-" , avg_salary)

#3. Median() :- Return the median of values

median_age = df["Age"].median()
print(f"Median of age : \n {median_age}")

#4. MIN / MAX() :- Return minimum and maximum values in each column.

Min = df["Age"].min()
Max = df["Age"].max()
print(f"Minimum Number in age :- {Min} , \n Maximum Number in age :- {Max}")

#5. COUNT() :- Count the non-null values in each column

Count = df["Age"].count()
print(Count)

#6.STD / VAR() :- Find standard deviation and variance
Std = df["Salary"].std()
Var = df["Salary"].var()

print(f"Standard Deviation :- {Std} \n Variance :- {Var}")

#DESCRIBE () :- Generates descriptive statistics
print(df.describe())

# AGG() / AGGREGATE() :- Allows multiple aggregation functions to be applied.
# df.agg(['sum', 'mean'])
# print(f"Single time using 2 aggregation function :- {df}")

# Specific columns
Col_Agg = df.agg({'Age' : ['mean' , 'max'] , 'Salary' : 'mean'})
print(f"Aggregate Specific Columns :- {Col_Agg}")

print(f"Unique values : \n{df.nunique()}")

#MODE() :- Return most frequent values

print(df.mode())

#quantile(q)
#Returns the q-th quantile.

print(df["Age"].quantile())

