name = input("Enter Your Name: ")
print (name)

# Input value alwasy store string datatype, using type casting to convert datatype

roll_number = input("Roll Number: ") # Save as a string value
print (type(roll_number))

roll_number = int(input("Roll Number: ")) # Save as a integer value
print (type(roll_number))

num1 = int(input("Enter Some Number: "))
num2 = int(input("Enter Some Number: "))

print ("The sum of", num1, "and", num2, "is", num1 + num2)