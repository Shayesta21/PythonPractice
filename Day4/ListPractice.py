#collections in python 1)list 2)tuple 3)set 4)dictionary

#list: it is changeable and ordered, it is written with a [], it is mutable
#Tuple: it is ordered and unchangeable collection, uses()
#Set: it is unordered and unindexed, uses{}
## Dictionary: it is used for key and value pairs, it is mutable and uses {} brackets

# how to create a list
list0=[12, 20, 30 ,40, 50]
list1=['apple', 'mango','banana', 'cherry']
list3=[10,'kite']
print(list)
print(list1)

#accessing items from a list
print(list1[0])
print(list[3])
print(list3[1])

#range of index

list5=['mother','father','brother','sister','grandpa','grandma']
print(list5[0:4])
print(list5[3:-1])
print(list5[-4:-1])

#change item on a list based on index
list5[0]="aunty"
print(list5)

#accessing items from a list with loop
for i in list5:
    print(i)

#check if item exists in the list using if statement
if'aunty' in list5:
    print("yes it is present")
else:
    print("no it is not present")

# find total no of items in a list
print(len(list5))

#add an item to a list: append or insert functions are available
#append will add the item in the end of the list
###APPEND###
list5.append("uncle")
print(list5)

###insert#####
#we can insert anywhere in the list
#the index value needs to be specified and the index of the next items will be moved
list5.insert(3,"child")
print(list5)

#remove item from the list: pop(), del, clear()
#pop()
list5.pop(3)
print(list5)

#del is a keyword and not a function: we need to give the index
del list5[2]

#clear(): it will clear all items from the list
list5.clear()
print(list5)

#copy a list
#1)using list()
lista=[1,3,44,5,556,6,]
listb=list(lista)
print(lista)
print(listb)

#2)using copy()
listb=lista.copy()
print(listb)

#combining 2 lists
#1) using + operator
listc=[1,2,3,4,5]
listd=[6,7,8,9,10]
liste=listc+listd
print(liste)

#using a loop
list11=[4,5,3,2,1]
list12=[3,5,6,7,8,8]

for i in list12:
    list11.append(i)
print(list11)

#using extend()
list13=[4,5,3,2,1]
list14=["a",'b','c']
list13.extend(list14)
print(list13)

#comparing 2 lists
list13=[4,5,3,2,1]
list14=["a",'b','c']
if list13==list14:
    print("they are equal")
else:
    print("they are not equal")