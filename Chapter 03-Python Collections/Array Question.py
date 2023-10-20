# Given a list in python and provided the index of the element.
# write a programe to swap the two swap elements in the list.

n = int(input("Enter size of the list: "))

list = []

for _ in range(n):
    num = int(input("Enter Number: "))
    list.append(num)

idx1 = int(input("Enter Index 01: "))
idx2 = int(input("Enter Index 02: "))

print(list)

# Swapping List

temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)
