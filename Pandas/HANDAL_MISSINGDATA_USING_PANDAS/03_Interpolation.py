# IF YOU HAVE A MISSING DATA SO REMOVE THE ROWS AND COLUMNS THAN A BATTER OPTION IS INTERPOLATION

# WHAT IS INTERPOLATION ?
# -> A Interpolation method fill the missing values using it's up and down data

# -> A interpolation method have so many types
# * Linear Method
# * Time Series Data Method
# * Polynomial Method
# * Avoiding Dropping Rows

# EXAMPLE

import pandas as pd

data = pd.read_csv("Updated_Employee_Data.csv")

df = pd.DataFrame(data)
print(df)

#LINEAR INTERPOLATION METHOD :-

df["Salary"]= df["Salary"].interpolate(method="linear")
print("After Interpolation Method Salary Result is :-")
print(df)