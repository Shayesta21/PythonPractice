#for loop

# print numbers 1-10

for i in(range(11)):  # output: 0,10
    print(i)

#print numbers 1- 10

for i in(range(1,11)): #output: 1,10
    print(i)

#print only even numbers 1-10

for i in (range(0,10,2)):    #output: 0 2 4 6 8
    print(i)

#print odd numbers 1-10
for i in(range(1,10,2)):   #output 1 3 5 7 9
    print(i)

#print numbers in descending order
for i in range(10,0,-1):
    print(i)

#print number 5- 100 increase by 5
for i in range(5,105,5):
    print (i)


#break command
for i in range(1,10):
    if i==5:
     break
    print(i)
print ("program is finished")

#continue (we can use it to skip numbers)
for i in range(1,11):
    if i==5:
        continue
    print(i)
print("program is completed")

for i in range(1,11):  #skipped 2, 5 , 7
    if i==2 or i==5 or i==7:
        continue
    print(i)