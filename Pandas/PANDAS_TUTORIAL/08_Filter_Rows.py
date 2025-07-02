import pandas as pd

datas = {
    "Name" : ["Yash","Ajay","Vijay","Jay","Aman","Akash"],
    "Age" : [20,21,20,19,20,20],
    "Salary" : [40000,20000,25000,32100,25000,850201],
    "Score" : [85,45,98,63,25,88]
}

df = pd.DataFrame(datas)
#It's a single condition to find and filter 1 rows
high_salary = df[df['Salary'] > 25000]
print(f"Filter Employee with 25000+ Salary :-\n {high_salary} ")

#Multiple condition to find and filter rows
salary = df[(df['Salary'] > 20000) & (df['Salary'] <= 25000)]
print(f"Employee Who Earned 20-25k :- \n {salary}")
