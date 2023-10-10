# "And" or "Or" operators

English_marks = int(input("Enter Your English marks: "))
Physics_marks = int(input("Enter Your Physics marks: "))

if English_marks > 80 and Physics_marks > 80:
    print("Congratulations, Your are eligible for final round")
elif English_marks > 80 or Physics_marks > 80:
    print("Ohh, You have last chance to eligible for final round")
else:
    print("Sorry, You repeat again this class")


# Take positve integers input and tel if it is a four digit number or not

Number = int(input("Enter a number: "))

if Number >= 1000 and Number <= 9999:
    print(Number, "is four digit number")
else:
    print(Number, "is not four  digit number")


# Take three positive integers input and print the greatest number

num_1 = int(input("Enter num_1: "))
num_2 = int(input("Enter num_2: "))
num_3 = int(input("Enter num_3: "))

if num_1 > num_2 and num_1 > num_3:
    print(num_1, "is greater than", num_2, "and", num_3)
elif num_2 > num_1 and num_2 > num_3:
    print(num_2, "is greater than", num_1, "and", num_3)
elif num_3 > num_1 and num_3 > num_2:
    print(num_3, "is greater than", num_1, "and", num_2)
else:
    print("Some problem, i thing your two or three input is same")