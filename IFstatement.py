# i=10
# if(i>15):
#     print("10 is less than 15")
# print("Iam Not in if")
#.............................................................
# i=20
# if(i<15):
#     print("i is smaller than 15")
#     print("im in if block")
# else:
#     print("i is greater than 15")
#     print("im in else block")
# print("im not in if and not in else block")
#.............................................................
# i=10
# if(i==10):
#     if(i<15):
#         print("i is smaller than 15")

#     if(i<12):
#         print("i is smaller than 12 too")
#     else:
#         print("i is greater than 15")
#.............................................................
# i=20
# if(i==10):
#     print("i is 10")
# elif(i==15):
#     print("i is 15")
# elif(i==20):
#     print("i is 20")
# else:
#     print("i is not present")
# ............................................................
# a=int(input("Enter a number: "))
# if(a%2==0):
#     print("The number is even")
# else:
#     print("The number is odd")
# .............................................................
# a=int(input("Enter a number: "))
# if(a>0):
#     print("the num is +ve")
# elif(a<0):
#     print("the num is -ve")
# else:
#     print("the num is 0")
# ..............................................................
# a=input("Enter a character")
# if a in ['a','e','i','o','u','A','E','I','O','U']:
#     print("It is a vowel")
# else:
#     print("It is not a vowel")
# ..............................................................
# Q:grading system create where u enter marks and grade is given
# mark=int(input("Enter the mark: "))
# if(mark<=100 and mark>=0):
#     if(mark==100):
#         print("O grade")
#     elif(mark>=85):
#         print("A grade")
#     elif(mark>=70):
#         print("B grade")
#     elif(mark>=55):
#         print("C grade")
#     elif(mark>=40):
#         print("P grade")
#     elif(mark<40):
#         print("YOU HAVE FAILED!!!!!!")
# else:
#     print("ENTER A VALID GRADE")

# print("1.Add\n","2.Subtract\n","3.Multiply\n","4.Divide\n")
# op=int(input("SELECT AN OPERATION: "))

# if(op==1):
#     n1=int(input("Enter the first number: "))
#     n2=int(input("Enter the second number: "))
#     sum=n1+n2
#     print(sum)
# elif(op==2):
#     n1=int(input("Enter the first number: "))
#     n2=int(input("Enter the second number: "))
#     sub=n1-n2
#     print(sub)
# elif(op==3):
#     n1=int(input("Enter the first number: "))
#     n2=int(input("Enter the second number: "))
#     mul=n1*n2
#     print(mul)
# elif(op==4):
#     n1=int(input("Enter the first number: "))
#     n2=int(input("Enter the second number: "))
#     if(n2>0 or n2<0):
#         div=n1/n2
#         print(div)
#     else:
#         print("Second number cannot be zero")
# else:
#     print("Enter a valid option!")
#................................................................
# print("Enter three numbers")
# a=int(input("First num: "))
# b=int(input("Second num: "))
# c=int(input("Third num: "))
# if(a==b and a==c):
#     print("All numbers are equal")
# elif(a>b and a>c):
#     print(a,"is the greatest number ")
# elif(b>a and b>c):
#     print(b,"is the greatest number ")
# else:
#     print(c,"is the greatest number ")
# ...............................................................
# yr=int(input("Enter the year: "))
# if(yr%4==0):
#     print(yr,"is a leap year")
# else:
#     print(yr,"is not a leap year")
# ...............................................................
# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=[]
# for i in l1:
#     if(i%2==0):
#         l2.append(i)
# print(l2)   
# ..............................................................
# l1=[1,2,3,4,5,6,7,8,9,10,11,12]
# l2=[]
# l3=[]
# n2=0
# n3=0
# for i in l1:
#     if(i%2==0):
#         l2.append(i)
#         n2=n2+i
#     else:
#         l3.append(i)
#         n3=n3+i
# print(l2)
# print("Sum of even numbers:",n2)  
# print(l3)
# print("Sum of odd numbers:",n3)  
  
    







  
