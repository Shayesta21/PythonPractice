# variable: a variable is a container that holds data
# type: global local
#global variables are created outside the functions
#local variables are created inside the functions are part of the function and cannot be accessed anywhere else

globalvar=200

def var():
    localvar=300
    print(localvar)
    print(globalvar)

var()

#to change the value of the global variable and print it
xy=300

def num():
    global xy
    xy=500
    print(xy)
num()
print(xy)

# when you do not declare a global variable and use global keyword directly in the function
#you can y=use the global variable inside the function, but you must declare the global keyword
def num():
    global a
    a=100
    print(a)
num()