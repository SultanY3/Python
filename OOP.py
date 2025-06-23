#creating objects:

# class Employee:
#     id=10
#     name="John"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# emp.display()

#deleting objects:

# class Employee:
#     id=10
#     name="John"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# del emp.id
# del emp.name
# emp.display()

#Object

# class car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)
# c1=car("Toyota",2016)
# c1.display()

#Non-parameterized Constructor

# class Student:
#     #Constructor - non parameterized
#     def __init__(self):
#         print("This is non parameterized constructor")
#     def show(self,name):
#         print("Hello",name)
# student=Student()
# student.show("John")

#Default constructor

# class Student:
#     roll_num=101
#     name="Joseph"

#     def display(self):
#         print(self.roll_num,self.name)
# st=Student()
# st.display()

#FULL

# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# #creates obj of class Student
# s=Student("John",101,22)

# #prints the attr name of the obj s
# print(getattr(s,'name'))

# #reset the attr name of obj s
# setattr(s,"age",23)

# # prints the modified value of age
# print(getattr(s,'age'))

# #prints true if the student contains the attr with name id
# print(hasattr(s,'id'))

# #deletes attr age
# delattr(s,'age')

# #this will give an error since the attr age has been deleted
# print(s.age)


#Homework

#1 . Create a class Student with attributes name, roll_number, and marks.Add a method to display student details.

# class Student:
#     marks=95
#     roll_num=101
#     name="Joseph"

#     def display(self):
#         print("Name:",self.name,"Roll no:",self.roll_num,"Marks:",self.marks)
# st=Student()
# st.display()

#2 . Create a class Rectangle with attributes length and width.Add a method to calculate and display the area.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         area = self.length * self.width
#         print("Area of the rectangle is:", area)

# rect = Rectangle(10, 5)
# rect.area()

#3 . Create a class Car with attributes brand, model, and year.Add a method to display full details of the car.

# class car:
#     def __init__(self,brand,modelname,year):
#         self.brand=brand
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print("Brand:",self.brand,"Model:",self.modelname,"Year:",self.year)
# c1=car("Toyota","Gr86",2019)
# c1.display()

#4 . Create a class Person with attributes name and age.Add a method to check if the person is eligible to vote (age ≥ 18).

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def check(self):
#         if self.age >= 18:
#             print(self.name,"is eligible to vote.")
#         else:
#             print(self.name,"is not eligible to vote.")

# person1 = Person("Afsal", 17)
# person1.check()

#5 . Create a class BankAccount with attributes account_holder and balance.Add methods to deposit, withdraw, and check balance.

# class BankAccount:
#     def __init__(self, account, balance=0): 
#         self.account= account
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance = self.balance + amount
#             print("Deposited:",amount)
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             print("Withdrew:",amount)
#         else:
#             print("Insufficient balance.")

#     def check_balance(self):
#         print("Accounts current balance:",self.balance)


# account = BankAccount("John", 1000)
# account.withdraw(300)
# account.deposit(420)
# account.check_balance()

#Q.Same question but use while true(dd monday)


# class BankAccount:
#     def __init__(self, account, balance=0): 
#         self.account = account
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print("Deposited:", amount)
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrew:", amount)
#         else:
#             print("Insufficient balance.")

#     def check_balance(self):
#         print("Account's current balance:", self.balance)


# account = BankAccount("John", 1000)

# while True:
#     print("\nChoose an action:")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")

#     choice = input("Enter choice (1-4): ")

#     if choice == '1':
#         amt = float(input("Enter amount to deposit: "))
#         account.deposit(amt)
#     elif choice == '2':
#         amt = float(input("Enter amount to withdraw: "))
#         account.withdraw(amt)
#     elif choice == '3':
#         account.check_balance()
#     elif choice == '4':
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice!")


