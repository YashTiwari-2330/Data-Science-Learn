import pandas as pd
from pandas import DataFrame

data = pd.read_csv("Updated_Employee_Data.csv")

df = DataFrame(data)
print(df)

#DROP METHOD :- ARE USE TO REMOVE UNWANTED COLUMNS IN DATA.
print("\n")
df.drop(columns=["Updated_Score"] , inplace=True)
print(f"After Removing A Updated_Score : \n {df}")