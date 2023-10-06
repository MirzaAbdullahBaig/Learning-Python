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
