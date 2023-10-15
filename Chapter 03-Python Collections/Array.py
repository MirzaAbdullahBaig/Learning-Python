# Python Collections (Arrays)
# Lists: These allows us to store multiple items in a single variable

fruits = ["Apple", "Banana", "Mango", "Cherry"]

print(fruits)
print(type(fruits))
print(len(fruits))

check_fruit = input("Enter correct fruit name: ")

# Checking the fruit available or not

if check_fruit in fruits:
    print(check_fruit, "is in the list")
else:
    print(check_fruit, "is not in the list")

# Accessing itmes of a list using indexes

print(fruits[2])
print(fruits[-2])
print(fruits[1:4])
print(fruits[-3:-1])