# # # # Adding items using append, insert and extend methods

# # # fruits = ["Apple", "Banana", "Mango", "Cherry"]

# # # fruits.append("orange")  # Using append to add itmes to end of the list
# # # fruits.insert(3, "Amrrod")  # Using insert to add itmes to index of the list

# # # new_fruits = ["Graps", "Lemon"]

# # # fruits.extend(new_fruits) # Using extend to add new list to another list

# # # print(fruits)


# # # # Removing items using remove and pop method

# # # fruits.remove("Amrrod") # Using remove to remove specified items from list
# # # fruits.pop(2) # Using pop to remove items at giving index or else last iten
# # # fruits.pop()

# # # print(fruits)


# # # #  Changing items using index number

# # # fruits[2] = "Dates"
# # # fruits[3:5] = ["Amrrod", "Graps"]
# # # print(fruits)

# # # # Sorting items using sort and reverse methods

# # # numbers = [60, 20, 30, 80, 50, 70, 40, 10]

# # # numbers.sort() # By default ascending
# # # print(numbers)

# # # numbers.sort(reverse=True) # Descending
# # # print(numbers)

# # # numbers.reverse() # Reseverse
# # # print(numbers)

# # # List Comprehension 

# # marks = [82, 90, 40, 10, 50, 30, 59]
# # students = ["Abdullah", "Adil", "Jalib", "Ahmed", "Zain", "Ahad"]

# # highest_mark = [i for i in marks if i > 80] 
# # A_students = [i for i in students if "A" in i]

# # print(highest_mark)
# # print(A_students)

# # # Copy and Concatenate Array using .copy method

# # mark = marks.copy() # copy array
# # All_marks = mark + highest_mark # Concatenate Array
# # print(All_marks)

# Nested List

friends = ["Adil", "Jalib", "Ahmed", ["Usman", "Fawad", "Mansoor"], "Shahmeer", "Ahad"]
print(friends)
print(friends[3][2]) 