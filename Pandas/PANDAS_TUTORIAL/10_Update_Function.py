# IF YOU WANT TO UPDATE ANY COLUMNS IN YOUR DATA SO YOU DO .LOC FUNCTION

import pandas as pd

datas = pd.read_csv("Updated_Employee_Data.csv")
df = pd.DataFrame(datas)
print(df)

#Do you want to update some specific rows in data so you can use .loc function
#df.loc(row_index , "column_name") = new_values

df.loc[0 , "Age"] = 21
print(f"Updated Yash Age :-\n {df}")

#But if you want to update whole data or large data than you use some conditions
df["Age"] = df["Age"] +2
print(f"Updated Whole Employees Age by +2 :- \n {df}")
