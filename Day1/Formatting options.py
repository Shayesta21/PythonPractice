#formatting print statements for output
name="John"
age=30
salary= 30000

#approach 1
print (name)
print(age)
print(salary)

#approach 2

print(name, age, salary)

#approach 3

print("name is= %s age is=%d salary is=%g" %(name, age, salary))

#approach 4
print ("name is:{} age is:{} salary is:{}" .format(name,age,salary))

#Taking input from users we use input() and for type conversion we use int() and float()
#this will concatenate the output and print and not add as the type of input here is string
num1=input("Enter your no: ")
num2=input("Enter your 2nd no: ")
print(num1+num2)
print(type(num1))

#in order to convert the output to int declare int before the input keyword or in the print statement
n1=int(input("enter your no:"))
n2=int(input("enter your 2nd no: "))
print(n1+n2)
print(type(n1))
#or
n1=input("enter your no:")
n2=input("enter your 2nd no: ")
print(int(n1)+ int(n2) )