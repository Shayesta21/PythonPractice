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
s="welcometopython"
print(s.isalnum())
print("2323".isnumeric())
print(s.isdigit())
print(s.islower())
print(s.isalpha())