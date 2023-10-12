num = int(input("Enter number: "))

for _ in range(num):
    print("*" * 5)


# Nested for loop

n = int(input("Enter number: "))

for i in range(n):
    for j in range(1, n+1):
        print(j, end="")
    print()

# practice

n = int(input("Enter number: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()


# practice

n = int(input("Enter Number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()

# practice

n = int(input("Enter Number: "))

for i in range(1, n + 1):           # loop for rows
    print(" " * (n-i), end="")      # printing spaces

    for j in range(1, 2 * i):
        print(j, end="")            # printing digits
    print()


# practice

n = int(input("Enter Number: "))

for i in range(1, n+1):              # loop for rows
    print(" " * (n-i), end="")       # printing spaces

    for j in range(1 , 2 * i):
        print(chr(64 + j), end="")   # printing characters
    print()