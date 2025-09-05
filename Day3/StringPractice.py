#Strings are immutable
#mutable: can be changed
#immutable: cannot be changed

# creating a string variable
s="welcome"
s1=''
s2=str("welcome")
s3=str('welcome')

#creating an empty string
n=""
n1=''
n2=str("")
n3=str('')

#to show string is immutable, here the value of the variable is changed which shows string is immutable
str1="welcome"
print(id(str1))

str1=str1+"to python"
print(id(str1))

# using + and * operator with strings
print("welcome"+"to python")


print("welcome to python "*3)

#Slicing operator []
#the index starts with 0
#ending index 1
str="welcome"
print(str[1:3])
print(str[:3])
print(str[4:])
print(str[1:-1])
print(str[1:-2])

#ord(): will give the ASCII no of the character and chr()
print(ord("a"))
print (chr(97))

#max() min() len()

print(max("a,n,z"))

print(min("anb"))

print((len("werlkjjdsjsdf")))

#in not in operator will return a bool value
srt="welcome"
print("come" in str)
print("wme" not in str)


#comparision operators in string
print("shay"=="shay") #true
print("teeth"<="tee") #false
print("men">="mens") #false
print("freedom"!="free")
print("abc"<" ")

#testing string functions return bool value
s="welcome to python"
print(s.isalnum())
print("2323".isnumeric())
print(s.isdigit())
print(s.islower())
print(s.isalpha())
print(s.isspace())

#Searching for substrings
s1="welcome to learning"
print(s1.startswith("wel"))
print(s1.endswith("come"))
print(s1.find("to"))
print(s1.find("learn"))
print(s1.find("my"))  #will return negative 1 (-1) as this is not present in the string
print(s.count("n"))  #returns the no of times the substring is present in the string

#converting strings
#capitalize(): will capitalize the first letter
m="string in Python"
m1=m.capitalize()
print(m1)

#title(): will capitalize each first letter in the string
m2=m.title()
print(m2)
#output:String In Python

#lower()
m3=m.lower()
print(m3)

#upper
m4=m.upper()
print(m4)

#swapcase
m5=m.swapcase()
print(m5)

#replace
m6=m.replace("in","to")
print(m6)

#####REVERSE A STRING########
#there is no direct logic to reverse
#2 methods: using for loop , using slicing operator eg: print(n[::-1])

# 1st method:
n="shayesta"
rev_str=""
for i in n:
    rev_str=i+rev_str
print("the reversed string is: "+rev_str)

#2nd method
n1="salam"
print(n1[::-1])