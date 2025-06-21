# ><><><><><><><><><><><>< Single Inheritence ><><><><><><><><><><><><

# syntax:
# class derived-class(base class)
#   <class-suite>

# Example:
# class Animal:
#     def speak(self):
#         print("Animal Speaking")
# #child class Dog inherits the base class Animal
# class Dog(Animal):
#     def bark(self):
#         print("Dog barking")
# d=Dog()
# d.bark()
# d.speak()

# ><><><><><><><><><><><>< Multi-Level Inheritence ><><><><><><><><><><><><

# Example:
# class Animal:
#     def speak(self):
#         print("Animal Speaking")
# #child class Dog inherits the base class Animal
# class Dog(Animal):
#     def bark(self):
#         print("Dog barking")
# #the child class Dogchild inherits another child class Dog
# class Dogchild(Dog):
#     def eat(self):
#         print("Eating bread...")
# d = Dogchild()
# d.bark()
# d.speak()
# d.eat()

# ><><><><><><><><><><><>< Multiple Inherintence ><><><><><><><><><><><><

# Example:
# class Calcutation1:
#     def Summation(self,a,b):
#         return a+b
# class Calcutation2:
#     def Multiplication(self,a,b):
#         return a*b
# class Derived(Calcutation1,Calcutation2):
#     def Divide(self,a,b):
#         return a/b
    
# d = Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))

# ><><><><><><><><><><><>< Heirarchical Inheritence ><><><><><><><><><><><><

# Example:
# #Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
# #Derived class1
# class Child1(Parent): 
#     def func2(self):
#         print("This function is in child 1.")       
# #Derived class2
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")

# obj1 = Child1()
# obj1.func1()  
# obj1.func2()  

# obj2 = Child2()
# obj2.func1()  
# obj2.func3()  

# ><><><><><><><><><><><>< Hybrid Inheritence ><><><><><><><><><><><><

# Example:
# class Office:
#     def office(self):
#         print("Office")
# class Desk(Office):
#     def PC(self):
#         print("There is a PC")
# class Deskchild(Desk):
#     def Printer(self):
#         print("There is a Printer")
# class Cupboard:
#     def USB(self):
#         print("There is a usb in the desk")
# class Workspace(Deskchild,Cupboard):
#     def Space(self):
#         print("This is my workspace")
# w1=Workspace()
# w1.Space()
# w1.office()
# w1.PC()
# w1.Printer()
# w1.USB()

# ><><><><><><><><><><><>< Polymorphism ><><><><><><><><><><><><

# Example 1:
# class Animal:
#     def speak(self):
#         print(Speaking")
# class Dog(Animal):
#     def speak(self):
#         print("Barking")
# d=Dog()
# d.speak()

# Example 2:

# class Bank:
#     def getroi(self):
#         return 10;

# class SBI(Bank): 
#     def getroi(self):
#         return 7;       

# class ICICI(Bank): 
#     def getroi(self):
#         return 8;

# b1 = Bank()
# b2 = SBI()  
# b3 = ICICI()  

# print("Bank Rate of interest:",b1.getroi());
# print("SBI Rate of interest:",b2.getroi());
# print("ICICI Rate of interest:",b3.getroi());

# Example 3:
# class Bird:
#     def intro(self):
#         print("There are many types of birds.")
#     def flight(self):
#         print("Most birds can fly but some cannot.")

# class Sparrow(Bird): 
#     def flight(self):
#         print("Sparrows can fly.")       

# class Ostrich(Bird): 
#     def flight(self):
#         print("Ostriches cannot fly.") 

# obj1=Bird()
# obj2=Sparrow()
# obj3=Ostrich()
# obj1.intro()
# obj1.flight()
# obj2.intro()
# obj2.flight()
# obj3.intro()
# obj3.flight()

# ><><><><><><><><><><><>< Abstract ><><><><><><><><><><><><

# from abc import ABC, abstractmethod
# class Animal(ABC):   # Abstract class
#     @abstractmethod
#     def make_sound(self):
#         pass # Abstract method
# class Dog(Animal): # Concrete class
#     def make_sound(self):
#         return "Woof!"
# class Cat(Animal): # Concrete class
#     def make_sound(self):
#         return "Meow!"
# # Client code
# dog=Dog()
# cat=Cat()
# print(dog.make_sound()) # Output: Woof!
# print(cat.make_sound()) # Output: Meow!