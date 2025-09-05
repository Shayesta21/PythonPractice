#conditional statements: 3 types
#1)if 2)if else  3)elif

#example 1
#to check if a person is eligible for vote
age=70
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")

#example 2 find if no is even or odd
n=15
if n%2==0:
    print("even")
else:
    print("odd")

#example 3 if else in a single line(ternary operator)
num=10
print("even") if num%2==0 else print("odd")

#example 4 if else with multiple print in single line
num=10
var={print("hello"),("world")} if num<10 else {print("hi"),("world")}

