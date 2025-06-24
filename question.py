# unit=int(input("Enter the amount of units used: "))
# price=0
# if unit>0 and unit<=100:
#     price=unit*5 
#     print("Bill:",price)
# elif unit>100 and unit<=200:
#     price=(100*5)+((unit-100)*8) 
#     print("Bill:",price)   
# elif unit>200:
#     price=(100*5)+(100*8)+((unit-200)*10) 
#     print("Bill:",price)  
# else:
#     print("Enter a valid amount!")



# ><><><><><><><><><><>< Leetcode Questions ><><><><><><><><><><><

# First unique character in a string

# s = input("Enter a string: ")
# if 1 <= len(s) <= 10**5:
#     for i in range(len(s)):
#         count=s.count(s[i])
#         if count == 1:
#             print(i)
#             break
#     else:
#         print("-1")
# else:
#     print("Enter string of valid length")

# Fisrt missing positive number

# 1<=num.length<=105
# -231<=nums[i]<=231.1

# nums = [2,3,1]
# i = 1
# while True:
#     if i not in nums:
#         print(i)
#         break
#     i+=1

# nums = [1, 3, 4, 5, 6]
# i = 1
# while True:
#     found = False
#     for j in nums:
#         if j == i:
#             found = True
#             break
#     if not found:
#         print(i)
#         break
#     i+=1

