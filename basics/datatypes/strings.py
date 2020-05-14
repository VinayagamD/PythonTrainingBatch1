mystring = 'This is my string'
print(mystring)
mystring = "this is my string test"
print(mystring)
# mystring = """
#             This is \n
#             my \n
#             string
#             """
print(mystring)
print(mystring[-1])
print(mystring[1])
print(mystring[0])
# for i in range(0,len(mystring)):
#     print(mystring[i], end="\t")
# print('====================================')
# for i in range(-1,-22):
#     print(mystring[i], end="\t")
print(mystring[0:5])
print(mystring[8:10])
# Find length of the string
print(len(mystring))
print(mystring[21])
print(mystring.upper())
print(mystring.lower())
print(mystring.capitalize())
hi = 'hi'
print(mystring + ' ' +hi)
print(mystring)

# Update String
mystring = 'T'+ mystring[1:]
print(mystring)
print(mystring[2:])
print(mystring[:5])

mystring = mystring[:5]
print(mystring)


mystring = "programiz"
extrated_string = mystring[5:-2]
print(extrated_string)
s = ('Hello' 'World')
print(s)

print('a' in mystring)
print('at' not in 'battle')

# enumurate
mystring = 'cold'
list_enumurate = list(enumerate(mystring))
print(list_enumurate)

mystring = 'i\'m vinay'
print(mystring)
print(mystring, '\n', mystring)
print("This is \x48\x45\x58 representation")
print(r"This is \x48\x45\x58 representation")

default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)
print('\n--- Positional Order ---')
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print(positional_order)
print('\n--- Keyword Order ---')
positional_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print(positional_order)

# Binary
print("Binary representation of {0} is {0:b}".format(12))
print("Binary representation of {0} is {0:e}".format(156.33))
print("Binary representation of {0} is {0:.3f}".format(2/3))
print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))

x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)

print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))
print('Happy New Year'.find('ew'))
print('Happy New Year'.replace('Happy','Brilliant'))

print('Ho '*3, 'Merry Christmas')
