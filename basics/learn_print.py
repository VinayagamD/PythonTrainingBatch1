"""
Mulitline comment
This is generally used for explaining class and methods
"""
'''
'''
# Single Line comment genrally used for the explaining variables and TODO:
# TODO : 
# Normal Print
print("Hi Midhul")

# Print with end
print("Hi Joshua", end='  ')
# print("Hi Joshua")
print("Hi Joshua", end='@')

print()
# Print with serparator
print("hi Midhul", "Your Learning Python Class", "Using Google Meets")
print("hi Midhul", "Your Learning Python Class", "Using Teams", sep=",")
print("hi Midhul", "Your Learning Python Class", "Using Teams", sep="\t")
print("hi Midhul", "Your Learning Python Class", "Using Teams", sep="\n")

# print file name
print_file = open("file.html", 'w+')
print("hi Anushka", "Your Learning Python Class", "Using Teams", file=print_file, flush=True)
