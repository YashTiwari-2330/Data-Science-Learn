# IN PANDAS IF YOU WORKING ANY LARGE DATA FILE
# AFTER YOU READ DATA AND COMPLETE MANIPULATION THAN YOU SAVE YOUR NEW CLEAN DATA INTO FRESH FILE SO WHAT CAN YOU DO?
# THAN PANDAS GAVE YOU SOME BUILT IN METHODS TO SAVE YOUR DATA INTO FRESH FILE

#EXAMPLE :-

import pandas as pd

data = {
    "Name" : ["Ram" , "Shyam" , "Ayan"],
    "Age" : [20,22,25],
    "City" : ["Ahmedabad" , "Delhi" , "MUMBAI"]
}

df = pd.DataFrame(data)
print(df)

# SAVE FILE INTO ANOTHER FILE AND YOU SAVE DATA INTO DIFFERENT FILE MODE LIKE(EXCL , JSON , CSV,ETC)

#1- FIRST WE SAVE FILE AS CSV
df.to_csv("Basic_Student_Data.csv" , index=False)

# 2- SECOND WE SAVE FILE AS EXCL
df.to_excel("Basic_Student_Data.xlsx" , index = False)

# 3- THIRD WE SAVE FILE AS JSON
df.to_json("Basic_Student_Data.json" , index = False)