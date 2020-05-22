"""
Studying about iteration
"""

for i in [1, 2, 3, 4, 5]:
    print(i)
print("Bye bye")

i = 1

while i < 5:
    print(i)
    i += 1

print("Bye bye")

for i in range(10):
    print(i)
print("exited for loop")
for i in range(1, 10):
    print(i)
print("exited for loop")
for i in range(2, 10, 3):
    print(i)
print("exited for loop")
print(list(range(1, 11)))
print(list(range(25, 0, -1)))
print("--------------- triangle number -----------------")
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()
print("--------------- matrix statement -----------------")
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print(" ")

print("--------------- break statement -----------------")
for i in range(1, 100):
    if i == 10:
        break
    print(i)

print("break the loop")

print("--------------- continue statement -----------------")
for i in range(1, 100):
    if i in range(1, 90):
        continue
    print(i)

print("continue the loop ended")

if i == 2:
    pass
