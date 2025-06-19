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
