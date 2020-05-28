"""
Here we are going to learn about lambda or anonymous function

Anonymous function means function without a function name

"""
from functools import reduce


def cube(x):
    """
    This function returns the cube value
    :param x: input number
    :return:  cube value of input
    """
    return x * x * x


print(cube(4))

cube_lambda = lambda x: x * x * x

print(cube_lambda(4))


"""
In lambda we have special functions such as map, filter, reduce
"""

# Filter in lambda -> filters the values

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 == 0), li))
print(final_list)

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

# Map for converting the values

final_list = list(map(lambda x: x*2, li))
print(final_list)

final_list = list(map(lambda x: chr(x), li))
print(final_list)

# Reduce
sum_list = reduce((lambda x, y: x + y), li)
print(sum_list)
