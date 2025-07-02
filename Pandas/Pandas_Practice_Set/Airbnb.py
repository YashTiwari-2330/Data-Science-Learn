import numpy as np
import pandas as pd

#Load dataset
df = pd.read_csv("Airbnb_Open_Data.csv")

#Viwe first few rows
print(df.head())

#View Columns
print(df.columns)

#Get basic information
print(df.info())

#Check the missing values
print(df.isnull().sum())

#2. DATA CLEANING

#-Drop duplicates
df.drop_duplicates(inplace= True)

#Drop columns with too many missing values
threshold = len(df) * 0.5
df = df.dropna(thresh=threshold , axis=1)

#Fill remaining missing values
df['price'] = pd.to_numeric(df['price'] , errors='coerce')
df['price'].fillna(df['price'].median() , inplace=True)

#Fill other important columns
df['NAME'].fillna("Unknown",inplace=True)
df['host name'].fillna("Unknown" , inplace = True)
df['last review'] = pd.to_datetime(df['last review'], errors='coerce')
df['last review'].fillna(pd.Timestamp("2020-01-01"),inplace=True)
df['host_identity_verified'].fillna("Unconfirmed" , inplace=True)
df['host name'].fillna("Unknown" , inplace=True)
df['neighbourhood group'].fillna("Unknown",inplace=True)
df['neighbourhood'].fillna("Undefined" , inplace=True)
df['lat'] = df['lat'].interpolate(method='linear')
df['long'].fillna("NaN")
df['country code'].fillna("US",inplace=True)
df['instant_bookable'].fillna("NaN",inplace=True)
df["cancellation_policy"].fillna("undefined",inplace=True)


#Show update null values
print(df.isnull().sum())
