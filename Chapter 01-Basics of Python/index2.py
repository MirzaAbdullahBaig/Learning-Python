# Arithmetic operaters

print ("Sum:", 4 + 3)
print ("Difference:", 4 - 3)
print ("Product:", 4 * 3)
print ("Division:", 4 / 3)
print ("floor Division:", 4 // 3)
print ("Remainder:", 4 % 3)
print ("Exponentiation:", 4 ** 3)

# Assignment operaters

num1 = 5
num2 = num1
print(num1, num2)

num2 += num1
print (num1, num2)

num2 *= num1
print (num1, num2)

num2 -= num1
print (num1, num2)

num2 /= num1
print (num1, num2)


# Comparison operaters

num1 = 4
num2 = 5
print (num1 == num2) #false
print (num1 != num2) #true
print (num1 > num2) #false
print (num1 < num2) #true
print (num1 >= num2) #false
print (num1 <= num2) #true


# Logical operaters

exp1 = 4 > 3
exp2 = 4 < 3

print("exp1 & exp2 with and operater", exp1 and exp2)
print("exp1 & exp2 with or operater", exp1 or exp2)
print("exp1 with not operater", not(exp1))
print("exp2 with not operater", not(exp2))

# Identity Operators

A = 4
B = 4
C = "Abdullah"

print ("A and B with (is) operator", A is B)
print ("A and C with (is) operator", A is C)
print ("A and B with (is not) operator", A is not B)
print ("A and C with (is not) operator", A is not C)


# Membership Operators ("in" or "not in")

# (in) Returns True if a sequence with the specified value is present in the object
# (not in) Returns True if a sequence with the specified value is not present in the object	

fruits = ["Mango", "Banana", "Apple"]

print ("If Apple is present in fruits: ", "Apple" in fruits)
print ("If Apple is not present in fruits: ", "Apple" not in fruits)


# Bitwise Operators (It's very hard)

bit1 = 5
bit2 = 3

print("bit1 and bit2 with bitwise & operator: ", bit1 & bit2)
print("bit1 and bit2 with bitwise | operator: ", bit1 | bit2)
print("bit1 and bit2 with bitwise XOR operator: ", bit1 ^ bit2)
