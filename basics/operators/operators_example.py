"""
Learning Operators
BODMAS -> (Brackets of Division Multiplication Addition and Subtraction)
"""

# Arithemtic
print("------------Arithmetic------------------")
print(2 + 4)
print(4 - 2)
print(4 * 2)
print(10 / 4)
print(10 % 4)
print(10 // 4)
print(2 ** 3)


# Comparision
print("------------Comparision------------------")
print(4 <= 5)
print(4 >= 5)
print(4 < 5)
print(4 > 5)
print(4 >= 4)
print(4 > 4)
print(4 <= 4)
print(4 < 4)
print(4 == 4)
print(4 != 4)

# Logical
print("-------------------Logical----------------------")
print("-------- and ------------------")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("-------- or ------------------")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("-------- not ------------------")
print(not True)
print(not False)

# Bitwise
print("------------------ Bitwise -------------------------")
print(7 & 6)
print(7 | 6)
print(~ 6)
print(2 >> 2)
print(2 << 2)
print(6 ^ 8)
print(7 ^ 6)

# Identity Operators
print("------------------ Special -------------------------")
print("------------------ Identity -------------------------")
u = "H"
x = "Hi"
x1 = "Hi"
y = "Hello"
z = 1
print(x is u)
print(x is x)
print(x is x1)
print(x is not y)
print(x is not z)

print("------------------ Membership -------------------------")
print(u in x)
print(u in y)
print(x in y)
print(x not in y)

print("------------- Short Hand Assigment -------------")
# LHS = RHS
x = 10
x += 5  # x = x+5
print(x)
