# Simple Practice using variables

name = "Abdullah"
roll_number = 123
percentage = 92.2
is_student = True

print (type(is_student))

print (name, roll_number, percentage, is_student)

# Update the values

name = "Muhamad"
print (name)

# lets try concatenate the values
# If you concatenate some values, you should use + sign if same datatypes if not you should use "," coma, otherwise you face the error

print ("My name is " + name + "and my roll number is ", roll_number)
print ("I am getting",percentage,"% marks in my class")

# lets try expression
print ("My percentage has been changed to", percentage - 1)

# lets try separator
print (name, roll_number, percentage, is_student, sep="-")

x = 1
y = 2
z = 3
print (x, y, z, sep= " -> ")

# Ascii (American Standard Code for Information Interchange) Let's try Ascii values

char = ("g")
print (ord(char))

ascii = (34)
print(chr(ascii))