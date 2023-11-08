#!/usr/bin/env python
# coding: utf-8

# In[1]:


#find the factorial number 
from math import sqrt, factorial
print(sqrt(16))
print(factorial(5))


# In[2]:


#importing sys.path and display the system path
import sys
print(sys.path)


# In[3]:


# import built-in module random
import math
print(dir(math))


# In[4]:


import string
print(dir(string))


# In[15]:


# python3 program explaining work
# of randint() function

# import random module
import random

# generate a random number between
# given position range
r1 = random.randint(5,15)
print("random number between -10 and -2 is % d" % (r1))


# generate a random number between
# tow negative range

r2 = random.randint(-15,-10)
print("random number between 15 and 10 is % d" % (r2))


# In[17]:


import random
print(random.randint(0,5))
print(random.random())
print(random.random()*100)
list=[1,4,True,800,"python",27,"hello"]
print(random.choice(list))


# In[18]:


import random
print(random.randint(0,5))


# In[19]:


print(random.random())


# In[20]:


print(random.random()*100)


# In[23]:


list=[1,4,True,800,"python",27,"hello"]
print(random.choice(list))


# In[28]:


#random module is imported
import random
for i in range (5):
    
#any number can be place in 0
    random.seed(1)
print(random.randint(1,1000))


# In[29]:


random.seed(2)
print(random.randint(1,1000))


# In[30]:


random.seed(3)
print(random.randint(1,1000))


# In[31]:


random.seed(4)
print(random.randint(1,1000))


# In[32]:


random.seed(5)
print(random.randint(1,1000))


# In[33]:


random.seed(6)
print(random.randint(1,1000))


# In[34]:


import math
print(math.sqrt(25))


# In[35]:


print(math.pi)


# In[36]:


print(math.degrees(2))


# In[37]:


print(math.radians(60))


# In[38]:


print(math.sin(2))


# In[39]:


print(math.cos(0.5))


# In[40]:


print(math.tan(0.23))


# In[41]:


print(math.factorial(4))


# In[51]:


import datetime
from datetime import time
import time

print(time.time())

print(date.fromtimestamp(454554))


# In[50]:


print(date.today())


# In[52]:


import platform
x=platform.system()
print(x)


# In[60]:


import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)
print(string.punctuation)


# In[67]:


from string import Formatter
f=Formatter()
print(f.format('{Website}',Website='journalDev'))


# In[69]:


from string import Template
t = Template("$name is the $title of $company")
s = t.substitute(name='pankaj',title='founder',company='journaldev')
print(s)


# In[1]:


import os


# In[3]:


import os
print(os.getcwd())


# In[5]:


entries = os.scandir(r'C:\Users\admin\Documents\vikas555')


# In[6]:


entries


# In[7]:


for i in entries:
    print(i.name)


# In[3]:


# oops concepts start now 03-oct
class student():
    def show(self):
        return "hello om"
ob=student()
ob.show()


# In[5]:


def show(self):
    return "hello om"
ob.show()


# In[7]:


class vehical():
    def type(self):
        return"hello omi"
ob=vehical()
ob.type()


# In[9]:


class teachers():
    def work(self):
        return "it's English teacher"
ob=teachers()
ob.work()


# In[10]:


class job():
    def type(self):
        return "its a employe on IT VEDANT"
ob=job()
ob.type()


# In[14]:


# you can create a multiple objects on same class 
class student(): # class header
    name="harri" #this name and age  are attributes
    age=20
    def show(self):           # self is first paramater and self its a variable
        name="vikas"
        age=22
        return f"my name is {name} and my age is {age} year old"     # f is consider to format in that sentence
# multiple objects are create on a single class
#class is an blueprint of an object

ob=student()
ob1=student()
ob2=student()
ob3=student()
ob.show()          # Accessing the object metod/attributes 
                    #object are creates then constructor automacally created in back side


# In[15]:


# multiple objects 
ob1=student()
ob.show()


# In[16]:


ob2=student()
ob.show()


# In[17]:


ob3=student()
ob.show()


# In[18]:


ob.age


# In[19]:


ob.name


# In[ ]:


# 04-oct

# object attributes 
#there are three ways to create the object attributes 
1. Directly define the attribute using objectname:
    objname.attribute=value
2.using object method
define common attribute for all the object method and then call that. but the problrm is don't call the method for some object then the attributes will not create for attributes

3.using


# In[2]:


class addition:
    f=0
    s=0
    result=0
    #constructor
    def __init__(self,f1,s1):      # f1 and s1 is instance variable
        self.f=f1
        self.s=s1
    def display(self):
        print("first number",self.f)
        print("second number",self.s)
        print("result",str(self.result))
    def cal(self):
        self.result=self.f+self.s
#creating ob of the class 
#this parameterize constructor
ob=addition(100,200)
ob.cal()
ob.display()


# In[16]:


class person:
    def eat(self,food,course="breakfast"):
        print(f'eating{food} for {course}')
    def sleep(self,hours):
        print(f'sleeping for {hours} hours')
    def walk(self):
        print("walking")
#object creation
Amit=person()
Ajay=person()
Aman=person()

print(id(Amit))
print(id(Ajay))
print(id(Aman))
#calling method with calls....      
Amit.eat("egg")
#calling method with object....
person.eat(Amit,'egg')

person.eat (Ajay,"Apple","snacktime")
Ajay.eat("Apple","snacktime")

Amit.sleep(10)
Amit.walk()

Ajay.sleep(2)


# In[ ]:


class person1:
    def seattribute(self):
        print(id(self))
        self.name=input("enter your name")
        self.age=int(input("enter your age"))
harry=person1()
jay=person1()
#object attribute
harry.name="harry potter"
jay.name="jay sharma"
#harry.age=13
#jay.age=15
person1.seattribute(harry)
print(id(jay))
prinnt(id(harry))
jay.seattribute()


# In[1]:


#05/oct

#types of constructors

#default constructor

class student:
    print("Hi,this is class using default constructor")
    
    def __init__(self):
        print("Hi this constructor is explicitly defined")
s1=student()


# In[3]:


class student():
    gender='male'       #class variable/static variable
    def __init__(self,name,age,rollno):     #constructor are created multiple variables
        self.name=name
        self.age=age                  #instance variable
        self.rollno=rollno 
    #def show(self):
        #print("display result",self.name)
ob=student("Ajay",21,101)
ob1=student("harish",21,102)
ob2=student("nitin",20,103)


# In[4]:


print(ob.name,ob.age,ob.rollno,ob.gender)


# In[5]:


print(ob1.name,ob1.age,ob1.rollno,ob1.gender)


# In[6]:


print(ob2.name,ob2.age,ob2.rollno,ob2.gender)


# In[23]:


class bank():
    branch="vashi"
    def __init__(self,name,age,Acno,amount):
        self.name=name
        self.age=age
        self.Acno=Acno
        self.amount=amount
        
ob=bank("vishal",21,1120003,2000)
ob1=bank("vinit",22,1210004,4000)
ob2=bank("omi",20,1320005,6000)
    


# In[24]:


print(ob.name,ob.age,ob.Acno,ob.amount,ob.branch)


# In[25]:


print(ob1.name,ob1.age,ob1.Acno,ob1.amount,ob1.branch)


# In[26]:


print(ob2.name,ob2.age,ob2.Acno,ob2.amount,ob2.branch)


# In[28]:


class A:
    x=20
    y=20
    def show(self):
        self.x=self.x+4
        A.y=A.y+4
        print("x=",self.x,"y=",self.y)
ob=A()
ob.show()


# In[29]:


A().show()


# In[30]:


A().show()


# In[31]:


ob.show()


# In[32]:


ob.show()


# In[33]:


class student:
    def __init__(self):
        print("hii,this is constructor without any parameter")
    def __init__(self,name):
        print("hii,this constructor with parameter")
        print("hello",name)
s1=student("vikas")


# In[34]:


class student:
    def __init__(self):
        print("hii,this is constructor without any parameter")
    def __del__(self):
        print("hii,this distractor with parameter")
s1=student()
        


# In[35]:


del s1


# In[2]:


#06/oct


class marks:
    @staticmethod
    def math_num(a,b):   #define the static math_num() function
         return a+b
    def sci_num(a,b):    #define the static sci_num() function
        return a+b
    def eng_num(a,b):    #define the static eng_num() function
        return a+b
#print the total marks in the maths
print("total marks in maths",marks.math_num(64,28))
#print the total marks in the science
print("total marks in science",marks.sci_num(70,25))
#print the total marks in the english
print("total marks in english",marks.eng_num(55,30))
    
    


# In[5]:


#inheritance strat now

#1. single inheritance : when child inherits from only one parent class, it is called single inheritance
#base class/super class
class parent:
    def function1(self):
        print("this is parent class")
#derive class/sub class
class child(parent):
    def function2(self):
        print("this is child class")
ob=child()
ob.function1()
ob.function2()


# In[8]:


# when a child class inherts from multiple parent class 

#base class1/super class
class Mother:
    mothername=" "
    def mother(self):
        (self.Mothername)
class father:
    Fathername=" "
    def father(self):
        print(self.fathername)
        
#derive class/sub class
class son(father,Mother):
    def parent(self):
        print("father",self.Fathername)
        print("Mother",self.mothername)
ob=son()
ob.Fathername="ABC"
ob.mothername="XYZ"
ob.parent()   
    


# In[ ]:


multilevel inheritance
fetures of the base class and the derived class are further inherited into the new derive class


# In[12]:


class first:
    def input1(self):
        self.a=int(input("Enter first number"))
        self.b=int(input("Enter second number"))
class second(first):
    def add(self):
        self.z=self.a+self.b
class Third(second):
    def result(self):
        print("sum of two number",self.z)
ob=Third()
ob.input1()
ob.add()
ob.result()


# In[ ]:




