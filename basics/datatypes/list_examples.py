"""
Learning about the list
"""

my_list = [] # Empty List
print(my_list)
my_list = ['Hi Joshua'] # List with string values 
print(my_list)
my_list = [["data11", "data12"] ,["data21", "data22"]]
print(my_list)

my_list = [10, 20.5, 3+5j, "Test", ["2d"]]
print(my_list)

print(my_list[1])
print(my_list[0])
print(my_list[4][0])
print(len(my_list))


# Add data to the list
my_list.append("20")
print(my_list)

#  Modify the data
my_list[0]=100
print(my_list)
my_list.insert( 7 ,"Inserted at 7")
print(my_list)

#  extending the list
my_list.extend(["One more list", "Aditional List"])
print(my_list)
print(my_list[-1])

#  removing the list
my_list.remove(100)
print(my_list)
my_list.pop()
print(my_list)
print("===================For each===============")
print("===================For each===============")
for data in my_list:
    print(data)
my_list.pop(2)
print(my_list)