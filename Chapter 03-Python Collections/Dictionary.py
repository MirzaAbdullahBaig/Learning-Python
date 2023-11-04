Student = {
    "Usman" : 737281,
    "Altaf" : 456576,
    "Jalib" : 547854,
    "Ahmed" : 989872,
}

print(Student)
print(type(Student))
print(len(Student))

print(Student["Ahmed"])
print(Student.get("Ahmed"))
print(Student.keys())

# update key's values

Student["Ahmed"] = 796766
print(Student)

#  add element in dictionary

Student["Ubaid"] = 788987
print(Student)

#  add another dictionary in dictionary

new_student = {
    "Muhammad": 788987,
    "Abdullah": 425356,
}

Student.update(new_student)
print(Student)

# Remove elements in dictionary

Student.pop("Ahmed")
print(Student)

# .popitem() this function removes last itme in dictionary

Student.popitem()
print(Student)

# .clear() this function removes all elements in dictionary

Student.clear()
print(Student)

# Printing values of a dictionary

Student = {
    "Usman" : 737281,
    "Altaf" : 456576,
    "Jalib" : 547854,
    "Ubaid" : 788987,
    "Muhammad" : 788987,
}

for x in Student: # Just print the keys
    print(x)

for x in Student: # Just print the values
    print(Student[x])

for x in Student.items(): # Print both keys and values
    print(x)

for x,y in Student.items(): # Print both keys and values separately
    print(x,y)

# Nested Dictionary

Student = {
    "Section_01" : {
        "A" : 1,
        "B" : 2,
        "C" : 3,
    },
    "Section_02" : {
        "D" : 4,
        "E" : 5,
        "F" : 6,
    }
}

print(Student["Section_01"]["C"])
print(Student["Section_02"])