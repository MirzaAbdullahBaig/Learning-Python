# Try These Question:

# Given a dictionary in python, write a program to find the sum of all items in the dictionary

dict_01 = {
    "a" : 100,
    "b" : 200,
    "c" : 300,
}

print("The sum of dict_01 value is:", sum(dict_01.values()))

dict_02 = {
    "x" : 25,
    "y" : 18,
    "z" : 45,
}

print("The sum of dict_02 value is:", sum(dict_02.values()))



# Given a string and a number N, we need to mirror the characters from the N-th position up to the length of the string in alphabetical order. In mirror operation, we change a to z, b to y, and so on.


input_string = input("Enter a string: ")
n = int(input("Enter n: "))

# Creating dictionary for mirror operation

alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dic1 = dict(zip(alphabets, reverse_alphabets))

# Finding the part of string on which we will do mirror operations

prefix = input_string[0 : n-1]
suffix = input_string[n-1 : ]

# finding a mirror string

mirror = ""
for i in range (0, len(suffix)):
    mirror = mirror + dic1[suffix[i]]

# Creating the final string

final_string = prefix + mirror
print("The result is: ", final_string)