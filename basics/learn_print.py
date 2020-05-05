"""
Mulitline comment
This is generally used for explaining class and methods
"""
'''
'''
# Single Line comment genrally used for the explaining variables and TODO:
# TODO : 
# Normal Print
print("Hi Joshua")

# Print with end
print("Hi Joshua", end='  ')
print("Hi Joshua")
print("Hi Joshua", end='@')

print()
# Print with serparator
print("hi Joshua", "Your Learning Python Class", "Using Teams")
print("hi Joshua", "Your Learning Python Class", "Using Teams", sep=",")
print("hi Joshua", "Your Learning Python Class", "Using Teams", sep="\t")
print("hi Joshua", "Your Learning Python Class", "Using Teams", sep="\n")

# print file name
printfile = open("file.txt", 'w+')
print("hi Joshua", "Your Learning Python Class", "Using Teams", file=printfile)