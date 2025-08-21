#Learning Comments in Python
# is used for a single line comment

#for multiple line comments use 3(""" or ''' use either or) in the beginning and in the end
""" 
these  are multiple line comments
"""
#to automatically add and remove comments use ctrl+/
# to comment multiple lines automatically use ctrl+shift+/

#keywords in python: these are reserved words
import keyword
print(keyword.kwlist) #prints all the keywords in python
#'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
# 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield'


#Data types in Python: it is dynamically typed declaring a data type for the variable is not required
"""
Text type       str
Numeric types   int float
sequence types  list tuple
Mapping type    dict
Set type        set
Boolean type    bool
"""
# eg: x=100 x="welcome" we can change the data type of x anytime
# to print the data type of the variable use the below code

x=100
print(type(x))

x="welcome"
y='welcome' #we can use single or double quotes for str and char in python, but in python single character is also str and not char
print(type(x))