# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇

tempA = a

a = b
b = tempA

# cleaner solution
# c = a
# a = b
# b = c

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
