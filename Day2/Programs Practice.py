#1) Write a program to print Positive no or negative no

n=-10
if n>=0:
    print("This is a positive no")
else:
    print("This is a negative no")

#2)Check the largest of 2 numbers

n1=100
n2=200

if n2>n1:
    print("This is the bigger no:",n2)
else:
    print("This is the bigger no",n1)

#3)check the largest of 3 numbers
n1, n2, n3= 500, 200, 300

if n1>n2:
    print(n1,"This is the greatest no")
elif n2>n3:
    print(n2,"This is the greatest no")
else:
    print(n3,"This is the greatest no")

#print week no if you provide week name as input

wn="Sunday"

if wn=="Sunday":
    print(1)
elif wn=="Monday":
    print(2)
elif wn=="Tuesday":
    print(3)
elif wn=="Wednesday":
    print(4)
elif wn=="Thursday":
    print(5)
elif wn=="Friday":
    print(6)
elif wn=="Saturday":
    print(7)
else:
    print("invalid day no")
