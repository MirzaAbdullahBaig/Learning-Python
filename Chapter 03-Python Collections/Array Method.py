# Adding items using append, insert and extend methods

fruits = ["Apple", "Banana", "Mango", "Cherry"]

fruits.append("orange")  # Using append to add itmes to end of the list
fruits.insert(3, "Amrrod")  # Using insert to add itmes to index of the list

new_fruits = ["Graps", "Lemon"]

fruits.extend(new_fruits) # Using extend to add new list to another list

print(fruits)


# Removing items using remove and pop method

fruits.remove("Amrrod") # Using remove to remove specified items from list
fruits.pop(2) # Using pop to remove items at giving index or else last iten
fruits.pop()

print(fruits)


#  Changing items using index number

fruits[2] = "Dates"
fruits[3:5] = ["Amrrod", "Graps"]
print(fruits)

# Sorting items using sort and reverse methods

numbers = [60, 20, 30, 80, 50, 70, 40, 10]

numbers.sort() # By default ascending
print(numbers)

numbers.sort(reverse=True) # Descending
print(numbers)

numbers.reverse() # Reseverse
print(numbers)