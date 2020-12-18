"""
Mulitline comment
This is generally used for explaining class and methods
"""
'''
'''
# Single Line comment genrally used for the explaining variables and TODO:
# TODO : I will need add some more functions
# Normal Print
print("Hi Akshaya")

# Print with end
print("Hi Pratiban", end='  ')
print("Hi Megha", end='  ')
# # print("Hi Joshua")
print("Hi Goutham", end='@')
print("Hi RajaShekar ", end='\t')
print("Welcome to python")

print()
# Print with separator
print("hi Prathiban", "Your Learning Python Class", "Using Pycharm")
print("hi Megha", "Your Learning Python Class", "Using Teams", sep=",")
print("hi Goutham", "Your will Learn Python Class", "Using Colab in future", sep="\t")
print("hi Akhsya", "Your already Learnt Python Code Execution", "Using Visual Studio Code in first class", sep="\n")

# print file name
print_file = open("file.html", 'w+')
print("<p>hi Anushka</p><br>", "<h3>Your Learning Python Class</h3>", "<p>Using Teams</p>", file=print_file, flush=True)
