#To check version
'''
import sys
print("python version : ")
print(sys.version)
print("version info. : ")
print(sys.version_info)
'''
#current datetimecomma 
'''
import datetime
now=datetime.datetime.now()#what this line of code means 2times use of datetime word
print("Current date and time :  ")
print(now.strftime("%Y-%m-%d %HH:%MM:%SS "))
'''
#area of circle
'''
from math import pi
r=float(input("Enter the radius of circle : "))
A=pi*r**2

print("Area of cicle : ",A)
'''
#reversed name print
'''
F=input("Enter the first name : ")
L=input("Enter the last name : ")
print("Hii "+L+" "+F)

or 

FL=(L+F)
print("your reversed name : ",FL)

'''
#Explain
#that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
'''
values=input("Enter some comma seperated numbers : ")
list=values.split(",")
tuple=tuple(list)
print("List : ",list)
print("Tuple : ",tuple)
'''
#shorter form
'''
x=input("Enter comma seperated values : ")#float and int cannot be used here

a=x.split(",")

l=list(a)
t=tuple(a)

print(l)
print(t)
'''
#Explain
#print extension of the file name
'''
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
print(type(filename))
'''
#or
'''
x=input ("enter file name : ")
n=x.index (".")
print (x [n+1:])
'''

#Print first and Last colour
'''
color_list = ["Red","Green","White" ,"Black"]
print("%s %s"%(color_list[0],color_list[-1]))
'''
#To print short form of any name
'''
x=input("Enter Full Name : ")
print(x[0].upper(),".",end="")

for i in range (0,len(x)):
    if x[i]==" ":
        print(x[i+1].upper(),end="")
'''
#or
'''
x=input("Enter Full Name : ")

x=x+" "

e=""

for i in range(0,len(x)):
    if x!=" ":
        e=e+x[i]
    else:
        if i!=len(x)-1:
            print(e[0].upper(),".",end="")
            e=""
        else:
             print(e.capitalize())
'''
    
#or by using function
'''
def name(s):
    l=s.split()
    new=""
    for i in range(len(l)-1):
         s=l[i]
         new+=(s[0].upper()+'.')
         new+=l[-1].title()
         
    return new

s=input("Enter Full Name : ")
print(name(s))
'''
#recurtion: it is a function which calls itself
'''
n=float(input("Enter Number : "))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

res=fact(n)
print("Factorial is : ",res)
'''
#accepts the value and print in n+nn+nnn
a=int(input('Enter Number : '))
n1=int("%s" % a)
n2=int("%s%s" % (a,a))
n3=int("%s%s%s" % (a,a,a))
print(n1+n2+n3)
