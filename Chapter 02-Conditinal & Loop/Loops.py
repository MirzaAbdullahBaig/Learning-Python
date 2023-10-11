# for loop

for i in range(1, 10):
    print(i, "Hello world!")

# Print elements of the list using for loop

students = ["Abdullah", "Adil", "Jalib", "Ahmed", "Bilal"]
fruits = [10, 20 , 30, 40, 50]

for i in students:
    print(i)

# While Loop

# Practice 01

i = 2
while i <= 30:
    print (i)
    i += 2


# Practice 02

j = 0
while j <= 10:
    print (j)
    j = j + 1


# Practice 03

x = 1
while x == 1:
    x = x -1
    print ("Value X", x)


# Practice 04

x = 4
y = 0

while x >= 0:

    x -= 1
    y += 1

    if x == y:
        print("X and Y are equal")
    else:
        print("X and Y are not equal")


# Practice 05

g = 4
h = 0

while g >= 0:

    if g == h:
        break
    else:
        print(g, h)

    g -= 1
    h += 1