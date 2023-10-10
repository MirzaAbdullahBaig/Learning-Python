# Basic calculator by using Match case

num_1 = int(input("Enter num_1: "))
num_2 = int(input("Enter num_2: "))

print("Select Operators: +, -, *, /, //, **, %")

operator = input("Enter operator: ")

match operator:
    case "+":
        print("Sum of", num_1, "and", num_2, "is", num_1 + num_2)
    case "-":
        print("Difference of", num_1, "and", num_2, "is", num_1 - num_2)
    case "*":
        print("Multiply of", num_1, "and", num_2, "is", num_1 * num_2)
    case "/":
        print("Division of", num_1, "and", num_2, "is", num_1 / num_2)
    case "//":
        print("Floor Division of", num_1, "and", num_2, "is", num_1 // num_2)
    case "**":
        print("Exponentiation of", num_1, "and", num_2, "is", num_1 ** num_2)
    case "%":
        print("Modulus of", num_1, "and", num_2, "is", num_1 % num_2)
    case _:
        print("Enter a valid operator")