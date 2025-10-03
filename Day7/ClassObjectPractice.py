#A class is a collection of variables and methods
#it is a logical entity, it does not occupy space in the memory

#object: an object is an instance of a class, it is a logical entity, it occupies space in the memory

#to declare a class use the class keyword
#we can create an instance method and static method
#instance method call through an object
#static method call through the class name

#####instance methods
class mytestclass:
    def testfun(self):
        pass

    def testfun1(self, name):
        print(name)


mtc = mytestclass()
mtc.testfun1("shay")


class thisclass:
    def thisfun(self, a, b):
        return a + b


th = thisclass()
print(th.thisfun(10, 20))


class learnclass:
    @staticmethod
    def learnfun(self, num):
        print(num)


print(learnclass.learnfun(300, 400))


#declaring and using class variables
class TestCV:
    a, b = 20, 40  # class variables

    def add(self):
        print(self.a + self.b)

    def mul(self):
        print(self.a * self.b)

    def sub(self):
        print(self.a - self.b)


# Create an object
tv = TestCV()

# Call methods
tv.add()
tv.mul()
tv.sub()

#using class, global and local variables together
a, b = 10, 20  #global variables


class tv1:
    a, b = 50, 60  #class variables

    def add(self, a, b):  #local variables
        print(a + b)
        print(self.a + self.b)
        print(globals()['a'] + globals()['b'])


testtv1 = tv1()
testtv1.add(30, 40)

###CONSTRUCTOR#####
# default parameter(this is not using any parameter)
class myclass1:
     def __init__(self):
         print("This is a constructor")

mc=myclass1()  #automatically invokes

#parameterised constructor
class mc2:
    name="john"
    def __init__(self,name):
        print(name)
        print(self.name)
m=mc2("fin")  #this object is automatically invoked and takes a name parameter

#eg: create a class emp with a constructor which take eid, en, salary and call it using a display method
class emp:
    def __init__(self,eid,en, sal):
         self.eid=eid
         self.en=en
         self.sal=sal
    def display(self):
        print(self.eid,self.en,self.sal)


e=emp(101,"John",3000)
e.display()

e1=emp(102,"peter",30000)
e1.display()