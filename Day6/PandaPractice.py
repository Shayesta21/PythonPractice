import pandas as pd
#delcaring a dataset

ds1={
    "fruits":["apple","mango","banana"],
    "veggies":["tomato","potato","cucumber"],
    "meats":["fish","chicken","veal"]
}

myv=pd.DataFrame(ds1)
print(myv)

#declaring a series

a=[1,2,3]

myvar=pd.Series(a)
print(myvar)

#we can print the value of the variable with the index
print(myvar[2])
print(myvar[1])

#creating your own index
myvar=pd.Series(a,index=["e","b","c"])
print(myvar["e"])