names = {"Abdullah", "Adil", "Jalib"}

print(names)
print(len(names))
print(type(names))

#  Add elements to set

names.add ("Ahad")
print(names)

# Accessing itmes of set

for x in names:
    print(x)

# Check if an item exists

if "Adil" in names:
    print("Adil is in set")


# Add another to the sequence

list = ["Zain", "Shahmeer"]
names.update(list)
print(names)


# Removing an item from the set

names.remove("Adil")
names.discard("Ahmed") #Discard function wil not throw error if vaue is not present in the set

print(names)


# Joining two set

a1 = {"a", "b", "c"}
a2 = {"d", "e", "a"}
print(a1, a2)

a3 = a1.union(a2)
print(a3)

a1.update(a2)
print(a1)

# Keep obly duplicates while joining

a1.intersection_update(a2)
print(a1)

# keep all values except duplicates

a1.symmetric_difference_update(a2)
print(a1)