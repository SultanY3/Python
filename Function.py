# def square(num):
#     return num**2
# object_=square(6)
# print("The square of the given number is:",object_)

# def square(num):
#     return num**2
# object_=square(int(input("Enter a number:")))
# print("The square of the given number is:",object_)

# def square(num):
#     return num**2
# a=int(input("Enter a number:"))
# b=square(a)
# print(b)

# def a_function(string):
#     "This prints the value of length of string"
#     return len(string)
# #calling the function we defined
# print(a_function("Functions"))
# print(a_function("Python"))
###########################
# #with arg with ret type

# #fn to calculate square of a number
# def square(num):
#     return num * num

# result=square(5)
# print("Square:",result)
##########################
# #with arg without ret type

# #fn to print greeting msg
# def greet(name):
#     print("Hello",name+"!")
# greet("Anu")
##########################
# #without arg with ret type 

# #fn that returns a welcome msg
# def get_msg():
#     return "Welcome to python programming" 
 
# msg=get_msg()
# print(msg)
##########################
# #without arg without ret type

# #fn to print numbers from 1 to 5 
# def print_num():
#     for i in range(1,6):
#         print(i)
# print_num()
##########################
#1
# def square(num):
#     return num * num
# result=square(int(input("Enter a number:")))
# print("Square:",result)
#2
# def sum_(num,num1):
#     return num + num1
# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# result=sum_(a,b)
# print("Sum of both numbers:",result)
#3
# def upper_fn(string):
#     return string.upper()
# a=input("Enter the string:")
# b=upper_fn(a)
# print(b)
#4
# def greet(name):
#     print("Hello",name+"!")
# a=input("Enter name:")
# greet(a)
#5
# def mult(n1,n2):
#     print("porduct:",n1*n2)
# n1=int(input("Enter 1st num:"))
# n2=int(input("Enter 2nd num:"))
# mult(n1,n2)
#6
# def even(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
# n=int(input("Enter num:"))
# even(n)
#7
# def get_year():
#     return 2025
# a=get_year()
# print("Current year:",a)
#8
# def get_msg():
#     return "Welcome to python programming" 
# msg=get_msg()
# print(msg)
#9
# def fact_5():
#     result = 1
#     for i in range(1,6):
#         result = result * i
#     return result
# print("Factorial:",fact_5())  
#10
# def nam():
#     print("your name is:",i)
# i=input("enter your name:")
# nam()
#11
# def print_num():
#     for i in range(1,11):
#         print(i)
# print_num()
##########################
# fn arguments

# def funct(n1,n2=20):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("Passing only one argument")
# funct(30)

# def funct(n1,n2):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("Without using keyword")
# funct(n2=50,n1=20)

# anonymous fn

# lambda_=lambda argument1,argument2: argument1+argument2
# #calling fn and passing values
# print("Value of the function is:",lambda_(20,30))
# print("Value of the function is:",lambda_(40,50))

#python fn within another fn

# def word():
#     string='Python functions tutorial'
#     x=5
#     def num():
#         print(string)
#         print(x)
#     num()
# word()

#recursive fn

# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial(x-1))
# num=3
# print("The factorial of",num,"is:",factorial(num))

# working::
# factorial(3)
# 3*factorial(2)
# 3*2*factorial(1)
# 3*2*1
# 6


#class work
#1 . Write a function that takes a list of numbers and returns the maximum.

# def max_num():
#     li=[100,20,30,200,50]
#     n=0
#     for i in li:
#         if i>n:
#             n=i
#     print("Max is:",n)
# max_num()

#2 . Define a function that returns the reverse of a given string.

# def rev(str):
#     return str[::-1]
# string=input("Enter a string:")
# a=rev(string)
# print("Reverse of string is:",a)

#3 . Write a function that takes a string and counts the number of vowels.

# def count_v(string):
#     a=0
#     for i in string:
#         if i in ['a','e','i','o','u','A','E','I','O','U']:
#             a=a+1
#     print("The number of vowels:",a)
# str=input("Enter a string:")  
# count_v(str)

#4 . Create a function to check if a number is a palindrome.

# def palindrome(num):
#     if str(num)==str(num)[::-1]:
#         print("It is a palindrome")
#     else:
#         print("It is not a palindrome")
# n=int(input("Enter a number:"))
# palindrome(n)

#5 . Define a function that accepts a list and returns a new list with only even numbers.

# def even():
#     li=[1,2,3,4,5,6,7,8,9,10]
#     ev=[]
#     for i in li:
#         if i%2==0:
#             ev.append(i)

#     print(ev)
# even()

#6 . Write a function that calculates the power of a number (without using ** or pow).

# def power(num, p):
#     result = 1
#     for i in range(p):
#         result = result * num
#     print("power:", result)
# n1=int(input("Enter number:"))
# n2=int(input("Enter power:"))
# power(n1,n2)
    
#7 . Create a menu-driven program using functions:

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     if b!=0:
#         return a/b
#     else:
#         print("Cannot divide by 0!")

# def menu():
#     while True:
#         print("\nMENU:")
#         print("1.ADD")
#         print("2.SUBTRACT")
#         print("3.MULTIPLY")
#         print("4.DIVIDE")
#         print("5.EXIT")

#         choice=int(input("Enter your choice:"))

#         if choice == 5:
#             print("Exiting...")
#             break

#         num1=int(input("Enter 1st number:"))
#         num2=int(input("Enter 2nd number:"))

#         if choice == 1:
#             print("Result:",add(num1,num2))
#         elif choice == 2:
#             print("Result:",sub(num1,num2))
#         elif choice == 3:
#             print("Result:",mul(num1,num2))
#         elif choice == 4:
#             print("Result:",div(num1,num2))
#         else:
#             print("Enter a valid choice!")

# menu()

#Homework

#1 . Write a recursive function to print numbers from n to 1.

# def print_num(n):
#     if n != 0:   
#         print(n)
#         print_num(n - 1)
# n1=int(input("Enter a number:"))
# print_num(n1)

#2 . Write a recursive function to calculate the sum of first n natural numbers.

# def sum_num(n):
#     if n != 0:
#         return n + sum_num(n - 1)
#     else:
#         return 0
# n1 = int(input("Enter a number: "))
# print("Sum:", sum_num(n1))

#3 . Write a recursive function to find the sum of digits of a number.

# def sum_dig(n):
#     if n!=0:
#         return n % 10 + sum_dig(n // 10)
#     else:
#         return 0
# n1 = int(input("Enter a number: "))
# print("Sum:", sum_dig(n1))

#4. Write a recursive function to reverse a string.

# def rev(s):
#     if len(s) == 0:
#         return s
#     else:
#         return rev(s[1:]) + s[0]
# txt = input("Enter a string: ")
# print("Reversed string:", rev(txt))

#1 . Write a lambda function to find the square of a number.

# lambda_=lambda n1: n1**2
# num=int(input("Enter a number:"))
# print("The square is is:",lambda_(num))

#2 . Write a lambda function to check if a number is even or odd.

# even = lambda n: "Even" if n % 2 == 0 else "Odd"
# num = int(input("Enter a number: "))
# print("The number is:", even(num))

#3 . Write a lambda function to find the maximum of two numbers.

# maximum = lambda n1,n2: n1 if n1>n2 else n2
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# print("The greater number is:", maximum(num1,num2))

#4 . Write a lambda function to check if a string starts with the letter 'A'

# string_= lambda s: "True" if s[0]=='A' or s[0]=='a' else "False"
# str = input("Enter a String: ")
# print("It is", string_(str),"that the string starts with A")
    







