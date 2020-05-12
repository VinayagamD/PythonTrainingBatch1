"""
Learn python data types
Sets basics
"""

#  Creating set
my_set = {1}
print(my_set)
print(type(my_set))
my_set = set()
print(my_set)
print(type(my_set))

my_set = {1 , 1, 4, 5,5, "Hello", "Hello", 5.5, 5.5}
print(my_set)
my_set.add("Hi")
my_set.add("Hello")
print(my_set)

my_list  = [1 , 1, 4, 5,5, "Hello", "Hello", 5.5, 5.5]
print(my_list)

my_set = set(my_list)
print(my_set)

for i in my_set:
    print(i)
    
my_set.remove('Hello')
print(my_set)
my_set.discard(5.5)
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)