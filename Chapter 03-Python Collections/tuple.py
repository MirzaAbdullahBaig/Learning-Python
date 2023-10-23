# practicing tuple

student = ("Ali", "Adil", "Abdullah", "Hamza", "Zain") # Tuple
name = ("Shahmeer",) # If Creating a tuple with 1 item then add come (,)
roll_num = tuple((1, 2, 3, 4, 5))

print(type(student))
print(len(student))


# Accessing the items in tuple

print(student[2]) # positive indexing
print(student[-2]) # negative indexing
print(student[1:4]) # Range indexing
print(student[-4:-2]) # negative range indexing



# Check if an item is in tuple

check_Student = input("Enter student name: ")

if check_Student in student:
    print(check_Student, "is in list")
else:
    print(check_Student, "is not in list")


# Traverse the tuple

for i in student:
    print(i)


# Concatenate tuples

All_friends = student + name

print(All_friends)

# Unpacking a tuple
student1, student2, student3, student4, student5 = student

print(student1, student2, student3, student4, student5)