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
