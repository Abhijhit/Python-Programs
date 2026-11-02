print("hello word") 
name="abhi"
age=21
salary=50000
age2=age
print(age2)
print(name)

#print sum
a = 4
b = 6 
sum = a + b
print(sum)
#1.Arithmetic operators
a=5
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
#Relational/comparison operators(==,!=,>,<,>=,<=)
a=15
b=5
print(a==b)
print(a!=b)
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
#assignment operator
num=10
num = num + 10#num+=10
print(num)

num=10
num**=10
print(num)

#logical operator
a=10
b=5
print(not False)

val = True
val2= False
print("and operator:",val and val2)

val = True
val2= True
print("or operator:",val or val2)

#Type conversion
a=int("5")
b=4.25
print(type(a))
print(a+b)
name=input("enter your name :")
print("welcome",name)
name=int(input("enter your name :"))
print("welcome",type(name),name)

#practice questions Write a program to input 2 numbers and print their sum
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
print("sum=",a+b)

#2 WAP to input side of a square and print its area
square=float(input("enter value of side:"))
print("area of square",square*square)#or Side**2

#3 WAP to input 2 floating point number and print their average
a=float(input("enter value 1 :"))
b=float(input("enter value 2:"))
print("average:",(a+b)/2)

#4 WAP to input 2 int numbers,a and b print true if a is greater than or equal to b.if not print false
a=int(input("first number:"))
b=int(input("second number:"))
if a>=b:
    print("True")
else:
    print("False")

"""or print(a>=b)"""