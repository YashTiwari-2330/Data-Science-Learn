# IF YOU FIND MISSING VAlUES IN DATABASE SO YOU HAVE 2 CHOICE
#1- IF YOU REMOVING MISSING VALUES
#2- YOU FILL THE VALUES WITH OTHER VALUES

import pandas as pd

data = pd.read_csv("Updated_Employee_Data.csv")

df = pd.DataFrame(data)
print(df)

#1- REMOVING MISSING VALUES

# df.dropna(inplace=True)
# print(f"Drop missing values :- \n {df}")

#2- IF YOU DETECT A MISSING VALUES SO YOU CAN REPLACE A MISSING VALUES WITH OTHER DATA

df["Salary"].fillna(df["Salary"].mean(), inplace = True)
print(f"Missing Values Replace With 0 :- \n {df}")

