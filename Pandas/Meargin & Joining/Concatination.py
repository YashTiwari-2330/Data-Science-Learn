# COMBINE DATA VERTICALLY(ROW) , HORIZONTALLY(COLUMNS)
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

#VERTICALLY COMBINE
con = pd.concat([customer , "\n" , order] , axis=0 ,ignore_index=True)
print(f"Combine Data as Vertically :- \n {con}")

#Horizontally Combine
hon = pd.concat([customer , order] , axis=1 , ignore_index=True)
print(f"Combine Data as Horizontally :- \n {hon}")