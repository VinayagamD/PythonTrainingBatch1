"""
Learn dictionary data structure basics
"""
my_dict = {}
print(my_dict)
print(type(my_dict))

my_dict = dict()
print(my_dict)
print(type(my_dict))

my_dict = {1: 'Apple', 2: 'Orange', 3: 'Banana'}
print(my_dict)


my_dict[4] = 'Apple'
print(my_dict)

print(my_dict[1])

my_dict.pop(1)
print(my_dict)

my_dict.clear()
print(my_dict)

my_dict = {'Fruits' : ['Apple', 'Banana'], 'Vegetable': ['Onion', 'Tomato']}
print(my_dict)