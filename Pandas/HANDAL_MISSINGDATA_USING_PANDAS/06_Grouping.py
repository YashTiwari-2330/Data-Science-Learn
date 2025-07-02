import pandas as pd

data = pd.read_csv("Updated_Employee_Data.csv")

df = pd.DataFrame(data)
print(df)

#Grouping :- Split data into small groups
Group = df.groupby("Name")["Updated_Score"].sum()
print(Group)

Group1 = df.groupby(["Name" , "Age"])["Salary"].min()
print(Group1)