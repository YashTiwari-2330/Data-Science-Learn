# In real life if we have data so that's not every time complete data we want some time data is not complete
# some data is incorrect some data is empty so how to handel this large data.

# NAN (Not a Number)

# NONE(For object data type)

# A PANDAS KNOW NAN DATA

#BEFORE HANDLING MISSING DATA FIRSTLY YOU KNOW WHERE DATA IS MISSING
# THAN WE USE ( ISNULL() ) METHOD

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

data = pd.read_csv("Updated_Employee_Data.csv")

df = pd.DataFrame(data)


a = df.isnull()
print(a)

# IF YOU CAN FIND HOW MUCH MISSING VALUES IN ALL COLUMNS SO USE THIS FUNCTION
count = df.isnull().sum()
print(count)
