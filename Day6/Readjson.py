import pandas as pd

df=pd.read_json("")
print(df.to_string())

#to string method will print all the values in the dataset
#when you only use print(df) the data of the first 5 rows will be printed