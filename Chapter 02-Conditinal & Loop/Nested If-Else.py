# Take three positive integers input and print the greatest number

num_1 = int(input("Enter num_1: "))
num_2 = int(input("Enter num_2: "))
num_3 = int(input("Enter num_3: "))

if num_1 > num_2:
    if num_1 > num_3:
        print(num_1, "is greater than", num_2, "and", num_3)
    else:
        print(num_3, "is greater than", num_1, "and", num_2)
else:
    if num_3 > num_2:
        print(num_3, "is greater than", num_1, "and", num_2)
    else:
        print(num_2, "is greater than", num_1, "and", num_3)


# Take positive integer input an tell if it is divisible by 3 and 5 but not divisible by 15

number = int(input("Enter a number: "))

if number % 3 == 0 or number % 5 == 0:
    if number % 15 == 0:
        print (number, "is divisible by 15")
    else:
        print(number, "is divisible by 3 and 5 but not divisible by 15")
else:
    print(number, "is not divisible by 3 and 5")