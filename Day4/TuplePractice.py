#Tuple: it is ordered and unchangeable collection
#it uses () brackets, it is immutable

# How to create a tuple

mytuple=('apple','banana','cherry', 'mango','grapes')
print(mytuple)

#creating an empty tuple
tuple1=()

#to access tuple items:
print(mytuple[0])
print(mytuple[-1])

#with range of indexes
print(mytuple[2:5])

#to change tuple values we will have to convert the tuple into list as the tuple is immutable
mylist=list(mytuple)
mylist[3]="melon"
mytuple=tuple(mylist)
print(mytuple)

#reading tuple items using a loop
for i in mytuple:
    print(i)

#to check if an item is present in a tuple
if "mango" in mytuple:
    print("yes it is present")
else:
    print("no it is not present")

#check the no of items in a tuple
print(len(mytuple))

#adding items to a tuple : this is not possible as it is immutable it gives the error
#Tuples don't support item assignment, TypeError: 'tuple' object does not support item assignment
"""
mytuple1=(1,2,3)
mytuple1[0]="4"
print (mytuple)
"""
 #copy tuple
tuple1=('apple','banana','cherry', 'mango','grapes')
tuple2=tuple1
print(tuple2)

#removing items form a tuple: it is not possible as tuple is immutable
tuple1=('apple','banana','cherry', 'mango','grapes')
#tuple1.remove('apple')#invalid this operation is not possible

#del mytuple
#print(mytuple)

#joining a tuple using '+'
tuplea=('apple','banana','cherry', 'mango','grapes')
tupleb=('2','3','4')
tuplec=tuplea+tupleb
print(tuplec)

#comparing tuple values
tuple21=('apple','banana','cherry', 'mango','grapes')
tuple22=('2','3','4')

if tuple21 == tuple22:
    print("tuples are equal")
else:
    print("tuples are not equal")

