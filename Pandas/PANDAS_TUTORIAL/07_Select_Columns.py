import pandas as pd

datas = {
    "Name" : ["Yash","Ajay","Vijay","Jay","Aman","Akash"],
    "Age" : [20,21,20,19,20,20],
    "Salary" : [40000,20000,25000,32100,25000,850201],
    "Score" : [85,45,98,63,25,88]
}

df = pd.DataFrame(datas)
print(f"Sample Dataframe :- \n{df}")

#IF YOU GOT ANY SINGLE COLUMNS SO USE THIS
print(f"Names (Single Columns) :-\n {df["Name"]}")

# IF YOU NEED MULTIPLE COLUMNS SO USE THIS
print(f"Multiple Columns :-\n {df[['Name' , 'Age']]}")

