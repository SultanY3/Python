# num=[4,2,6,7,3,5,8,10,1,9,2]
# square=0
# squares=[]
# for value in num:
#     square=value**2
#     squares.append(square)
# print("The list of squares is:",squares)
#....................................................................
# string="Python loop"
# for s in string:
#     if s=="o":
#         print("If block")
# else:
#     print(s)
# ....................................................................
# print(range(15))
# print(list(range(15)))
# print(list(range(4,9)))
# print(list(range(5,25,4)))
# ....................................................................
# tu=("Python","Loops","Sequence","Condition","Range")
# for iterator in range(len(tu)):
#     print(tu[iterator].upper())
# ....................................................................
# r=int(input("Enter the range: "))
# s=0
# for i in range(r+1):
#     s=s+i
# print("Sum of items in range=",s)
# ....................................................................
# n=int(input("Enter the Number: "))

# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# n=int(input("Enter the number: "))
# if n<0:
#     print("fatorial is undefined")
# else:
#     f=1
#     for i in range(1,n+1):
#         f=f*i

# print("Factorial of",n,"is :",f)

# n=int(input("Enter the number: "))
# li=[]
# a,b=0,1
# print("Fibonnaci series:")
# for i in range(n):
#     li.append(a)
#     a,b=b,a+b
# print(li)

# n=int(input("Enter the range:"))
# sum=0
# for i in range(n):
#     if(i%2==0):
#         sum=sum+i
# print("Sum of all even numbers upto",n," is: ",sum)

# str=input("Enter a string: ")
# c=0
# for i in str:
#     if i in ['a','e','o','u','i','A','E','I','O','U']:
#         c=c+1
# print("the number of vowels in the sting is:",c)

# li=[100,20,330,69,87]
# max=li[0]
# for i in li:
#     if i>max:
#         max=i
# print("The greatest number in the list is:",max)

# li=[1,2,3,4,5]
# product=1
# for i in li:
#     product=product*i
# print("The product of all the numbers in the list is:",product)

# str=input("Enter a string:")
# rev=""
# for i in str:
#     # rev=str[::-1]
#     rev=i+rev
# print("Reverse is:",rev)


# str=input("Enter a string: ")
# l=len(str)
# e=[]
# for i in range(0,l,2):
#     e.append(str[i])
# print("Characters at even indecies are:",e)

# str=input("Enter a string: ")
# l=len(str)
# for i in range(0,l,2):
#     print("Characters at even index",i,"is:",str[i])


# n1=int(input("Enter number of elements of 1st list: "))
# l1=[]
# print("Enter",n1,"elements:")
# for j in range(n1):
    
#     l1.append(input())
# n2=int(input("Enter number of elements of 2nd list: "))
# l2=[]
# print("Enter",n2,"elements:")
# for _ in range(n2):
    
#     l2.append(input())
# com=[]
# for i in l1:
#     if i in l2 and i not in com :
#         com.append(i)


# print("Common elements are:",com)

n=int(input("Enter the number: "))
l=len(str(n))
sum=0
for i in range(0,l):                                 
    d=n%10
    sum=sum+d
    n=n//10    
print("Sum is:",sum)
#..................................................................
#WHILE LOOP

# count=10
# while count>0:
#     print(count)
#     count-=1

# num=int(input("Enter a number: "))
# sum=0
# while num>0:
#     dig=num%10
#     sum=sum+dig
#     num=num//10

# print("Sum of digits is:",sum)

# num=int(input("Enter a number:"))
# while True:
#     if num>0:
#         if str(num)==str(num)[::-1]:
#             print("The number is a palindrome")
#             break
#         else:
#             print("It is not a palindrome")
#             break

# num=int(input("Enter a number:"))
# while True:
#     if num>0:
#         c=len(str(num))
#         print("The  number of digits is:",c)
#         break

# txt=input("Enter some text:")
# while True:
#     if txt=="quit":
#         break
#     else:
#         txt=input("Enter some text:")


# num=int(input("Enter a number: "))
# digit=int(input("Enter a digit: "))
# count=0
# while num>0:
#     last=num%10
#     if last==digit:
#         count=count+1
#     num=num//10
# print("The number of times",digit,"is repeated is:",count)

# a=int(input("Enter the number: "))
# b=0
# c=0
# d=a
# while a>0:
#     b=a%10
#     c=c+b**3
#     a=a//10
# if c==d:
#     print("It is an armstrong number")
# else:
#     print("It is not an armstrong number")







    