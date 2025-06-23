# ><><><><><><><><><><>< Pickling ><><><><><><><><><><><

# How to use:

# import pickle
# # Data to be pickled 

# students=[{"name":"Alice","age":20},{"name":"Bob","age":22}]
# # writing to a file

# with open("students.pkl","wb") as file:
#     pickle.dump(students,file)

# Deserializing Objects(Unpickling using load)

# with open("students.pkl","rb") as file:
#     loaded_student=pickle.load(file)
# print(loaded_student)