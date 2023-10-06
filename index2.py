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