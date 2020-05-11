"""
Learn Tuple Data Type
"""

first_tuple = ()
print(first_tuple)

first_tuple = ('Hello', 1, 10.0, 3+1j)
print(first_tuple)

first_tuple = ( 1, 10.0, 3+1j, -1)
print(first_tuple)
print(first_tuple[0])

# To test immutable
# first_tuple[0] = 'Joshua'
print(first_tuple)
my_list = [1,2,3,4,5]
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)
my_tuple[0]
print(my_tuple)
print(my_tuple)
my_tuple = my_tuple[1:]
print(my_tuple)