# MERGE MULTIPLE COLUMNS

import pandas as pd

customer = pd.DataFrame({
    "customer_id" : [101,102,103,104],
    "Name" : ["Yash" , "Ramesh" , "Suresh" , "Vijay"],
    "Buy" : ["Tv" , "Lcd" , "Mobile" , "LED"]
})

order = pd.DataFrame({
    "customer_id" : [101,102,104,105],
    "OrderAmount" : [25000,22000,32000,52000],
    "Order_place" : ["Ahmedabad" , "Delhi" , "Mumbai" , "Ahmedabad"]
})

#MERGE
#1- INNER JOINT :- Only Return Customer_id who are same in both data
Inner = pd.merge(customer , order , on="customer_id" , how="inner")
print(f"Inner Join Example :- \n {Inner}")

#2- OUTER JOINT :- Return all the values but some values are note match in both data so return NAN.
Outer = pd.merge(customer , order , on="customer_id" , how="outer")
print(f"\nOuter Joint Example :- \n {Outer}")

#FILL THE MISSING VALUES WITH 0
fill = Outer.fillna(0 , axis=0)
print(f"\nFill the missing values :- \n {fill}")

#3- LEFT JOINT :- Return the Left values as val as and Right side values gone miss match values return  NAN.
Left = pd.merge(customer , order , on = "customer_id" , how = "left")
print(f"Left Joint :- \n {Left}")

#4-RIGHT JOINT :- Right values show as well as but left values can not match so gave NAN.
Right = pd.merge(customer , order , on = "customer_id" , how = "right")
print(f"\nRight Joint :- \n {Right}")

#5- CROSS JOINT :- Merge both of the rows without compair.
Cross = pd.merge(customer , order  ,  how="cross")
print("Cross Joint :- \n" , Cross)