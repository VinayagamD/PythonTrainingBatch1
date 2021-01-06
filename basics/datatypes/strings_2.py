data = "Akshaya"
print(len(data))
print(data[2:4])
data = "This is example string to show demo of string"
print(len(data))
print(data[::-1])
print(data[-1:-len(data)-1:-1])
print(data[:-len(data)-1:-1])
print(data[6:])
print(data[:7])
print(data[::5])
print(data[::2])
print(data[0:len(data):2])

for i in range(0, len(data)):
    print(i, end="\t")
print()
for i in range(0, len(data)):
    print(data[i], end="\t")
print()

for i in data:
    print(i, end="\t")
print()
data = 'Megha'
print(data*10)
