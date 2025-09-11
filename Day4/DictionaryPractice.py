# Dictionary: it is used for key and value pairs, it is mutable and uses {} brackets

#declaring a dictionary
myd={ "boy":"salam",
       "girl":"shay",
       "kid":"faaz"
}
print(myd)

#accessing items from a dictionary
print(myd["boy"])
print(myd["kid"])

#Using get()
print(myd.get("girl")) #direct

#storing in a variable and using get
x=myd.get("boy")
print(x)

#changing values in a dictionary
myd["boy"]="firaz"
print(myd)

#printing items in a dictionary using loop
for i in myd:
    print(i) # prints only key

for i in myd:
    print(myd[i]) #prints only value

#using my value()
for i in myd.values():
    print(i)

#using items() and printing both values

for x,y in myd.items():
    print(x,y)

#check if the key exists in the dictionary
if "boy" in myd:
     print("yes")
else:
     print("no")

#find no of items in the dictionary
print(len(myd))

#adding items to a dictionary
myd["color"]="red"
print(myd)

#remove items from dictionary
myd.pop("color")
print(myd)

#using del
#del myd["girl"]

#copying a dictionary
myd1=myd
print(myd1)

#using copy()
myd2=myd1.copy()
print(myd2)


