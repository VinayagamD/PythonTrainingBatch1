"""
Learn basic function
"""


def even_number(number):
    """Function takes input number returns number is even or not"""
    return number % 2 == 0


print(even_number(3))
print(even_number(4))


def function_without_parameter():
    """Function without params"""
    print("Parameters less function")


function_without_parameter()


def even_number_2(number=2):
    """
    This function check the input number is even or odd
    :param number: params require by function
    :return: boolean result true or false
    """
    return number % 2 == 0


print(even_number_2())


def student(name, school):
    """

    :param name:
    :param school:
    :return:
    """
    print(f"Hi student your name is ${name} and studying in ${school}")


student(school="Test School", name="Test Name")


def variable_arguments(*vargs):
    """
    Functions with variable arguments
    This function requires vargs
    print the vargs to the console
    """
    for arg in vargs:
        print(arg)


variable_arguments("Hi", "Hello")


def variable_key_args(** kwargs):
    """
       Functions with keyword variable arguments
       This function requires vargs
       print the vargs to the console
       """
    for key, value in kwargs.items():
        print(key, value)


variable_key_args(test="test1")

