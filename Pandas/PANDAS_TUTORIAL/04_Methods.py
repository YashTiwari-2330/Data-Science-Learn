#HEAD AND TAIL :-
#Both are use to show data if you have large data so firstly show the data ,
#showing data and data have large amount so you can not check whole data than you check at upper some data and at the end of data.
# So check the upper and ends data we can use ['HEAD' and 'TAIL'] functions

#HEAD():-
import pandas as pd

df = pd.read_csv("Software_Professional_Salaries.csv")
print(f"\tDisplay  rows first :-\n{df.head()}")

#TAIL():-

print(f"\tDisplay Bottom's Rows :-\n{df.tail()}")

#INFO():-

print("\tDisplay Information About the dataset :-\n")
print(df.info())