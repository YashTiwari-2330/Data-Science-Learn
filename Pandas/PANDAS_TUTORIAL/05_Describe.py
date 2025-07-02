import pandas as pd

datas = {
    "Name" : ["Yash","Ajay","Vijay","Jay","Aman","Akash"],
    "Age" : [20,21,20,19,20,20],
    "Salary" : [40000,20000,25000,32100,25000,850201],
    "Score" : [85,45,98,63,25,88]
}

df = pd.DataFrame(datas)
print("Sample DataFrame :-")
print(df)
print("Descriptive statistics :-")
print(df.describe())