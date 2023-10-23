number = (1, 2, 3, 4, 5, 6)
list = []

for x in reversed(number):
    list.append(x)

output_tuple = tuple(list)

print(output_tuple)