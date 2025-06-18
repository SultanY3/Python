# What is enumerate()
# The enumerate() function in Python is used to add a counter to an iterable,such as a list, tuple, or string.
# It returns an enumerate object,which can be used to get both the index and the value while looping.

# The iterable is the object we want to loop through, and start is the optional parameter that allows us to...
# ...set the starting index (default is 0).


# Syntax
# enumerate(iterable, start=0)

# enumerate()         -The built-in function used to loop over an iterable and get index + value.
# iterable            -Any iterable object (like list, tuple, string, etc.) to loop through.
# start (optional)    -The index to start counting from (default is 0).

# Example 1:
# fruits = ["apple", "banana", "cherry","peach"]
# for  index,fruit in enumerate(fruits):
#     print(index,fruit)

# How it works:
# 1.fruits is a list with 4 items: ["apple", "banana", "cherry", "peach"].
# 2.enumerate(fruits) turns the list into an iterator that gives (index, value) pairs:
# (0, "apple")
# (1, "banana")
# (2, "cherry")
# (3, "peach")
# 3.The for loop unpacks each pair into index and fruit, then prints them.
# 0 apple
# 1 banana
# 2 cherry
# 3 peach

# Example 2:
# fruits = ["apple", "banana", "cherry","peach"]
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)

# # Example 3:
# for index, char in enumerate("hello",start=1):
#     print(index, char)


