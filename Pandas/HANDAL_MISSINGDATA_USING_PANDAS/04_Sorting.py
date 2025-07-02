import pandas as pd

data = {
    "Name": ['Yash', 'Ajay', 'Vijay', 'Akash'],
    "Age": [25, 32, 45, 21],
    "Salary": [10000, 250000, 21000, 80000]
}

df = pd.DataFrame(data)

# Sort by 'Name' first, then by 'Age'
df.sort_values(by=["Name"], ascending=[True], inplace=True)
df.sort_values(by=["Age"], ascending=True, inplace=True)
df.sort_values(by=["Salary"] , ascending=True , inplace=True)
df.sort_index(axis=0 , inplace=True)
print("Sorted by Name and Age:")
print(df)
