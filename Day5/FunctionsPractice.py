#function: a set of statements which will perform a task
#you have to 1)declare a function 2) you have to call or invoke a function
#2 types of functions:
# #built-in functions: already provided by python
# user defined functions: the user will create this function

#def is a keyword used to define a function
#you need to call the function with the function name

# defining a function
#eg:def myfun(): use def to define a function use a function name with() brackets and end with a ':'

###function with no parameter only printing a value
def myfun():
    print("I am a function")

myfun()   #to call a function just call the function name

def color():
    print("I am red")
color()

####function with a single parameter no return
def name(name):
    print("Hello",name)
name("Shayesta")

###function with multiple parameter and return value
def cal(a,b):
    return(a+b)
print(cal(10,20)) ## print using print statement

#we can store the return value in a variable to perform more actions
sum=cal(300,400)
print(sum)

#when an empty function is created with a return value not provide it will return none as the output

def fun():
    return
print(fun())

def fun1():
    i=10 # when you declare a value but not return it  will still return none
print(fun1())