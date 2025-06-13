# correct = "python123"
# password = ""
# while password != correct:
#     password = input("Enter password: ")
# else:
#     print("Correct password entered.")

# num=[1,2,3,4,5,6,7,8,9]
# target=10
# for i in num:
#     if i==target:
#         print("Number found!!")
#         break
# else:
#     print("Number not found!!")

# secret = 69 
# attempts = 3  
# for i in range(attempts):
#     user = int(input("Guess the secret number: "))
#     if user == secret:
#         print("Congratulations! You guessed the correct number.")
#         break 
# else:
#     print("Game over! You failed to guess the number.")   

# for i in range(4):
#     for j in range(6):
#         print("* ",end=" ")
#     print() 

# n=5 
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()   

# for i in range(5,0,-1):
#     for j in range(1, i + 1):
#         print(j,end=" ")
#     print()

# def calculate(price,tax=5):
#     return price + (price*tax/100)
# print(calculate(100))

# list1=["soap","detergent"]
# def add(item):
#     global list1
#     list1.append(item)
# add("shampoo")
# print(list1)

str="Python programming is fun"
for i in str:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
