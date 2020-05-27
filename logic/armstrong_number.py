def get_num_pos(num):
    position = []
    while num != 0:
        position.append(num % 10)
        num = num // 10
    return position

u_input = 371
values = get_num_pos(u_input)
max_face_value = len(values)
sumvalue = 0

for i in values:
    sumvalue += i ** max_face_value

print(sumvalue == u_input)
