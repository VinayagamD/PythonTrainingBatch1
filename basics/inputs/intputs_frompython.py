"""
Learning to take from users
"""

data = input("Enter a value")
print(data)
print(type(data))
if data.isdigit():
    data = int(data)
    print(type(data))
