import pandas as pd

df=pd.read_csv("C:\\Users\\Shaye\\OneDrive\\Desktop\\data.csv")

print(df.to_string())#--will print all the info in the dataset

#print(pd.options.display.max_rows)

print(df.head())#--will print the first 5 rows

print(df.tail())#--will print the last 5 rows

print(df.info())#--will print all the information of the dataset
