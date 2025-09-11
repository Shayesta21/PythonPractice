#set is a collection which is unordered and unindexed
#set is mutable
# we use {} for a set

#declaring a set
myset={1,2,3,4,5}
print(myset)

#Accessing data in a set can be done only with a loop as in is unordered, index will not work
myset={1,2,3,4,5}
for i in myset:
    print(i)

#checking if a value exists in a set or not: will return a boolean value true or false
myset={1,2,3,4,5}
print(1 in myset)
print('a' in myset)

#adding an item to a set using add() or update()
#add: only one item can be added
myset={1,2,3,4,5}
myset.add(6)
print(myset)

#update
myset={1,2,3,4,5}
myset.update("7,8,9")
print(myset)

#find number  of items in a set
print(len(myset))

#remove an item from a set: 2 methods remove() discard
#remove
myset={1,2,3,4,5}
myset.remove(1)
print(myset)
# when you remove something which is not present in the set you will get the error: 'keyError'

#discard
myset={1,2,3,4,5}
myset.discard(2)
print(myset)

#clear all items form a set
myset1={'a','s','f'}
myset.clear()
print(myset)

#del myset1
print(myset1) #NameError: name 'myset1' is not defined. Did you mean: 'myset'?

#joining 2 sets 2 methods: union() and update
set1={'apple','orange','banana'}
set2={'a','b','c'}
set3=set1.union(set2)
print(set3)

#update
set1={'apple','orange','banana'}
set2={'a','b','c'}
set1.update(set2)
print(set1)



