# Check number is positive or negative 

number = int(input("Check number is positive or negative, Enter any number: "))

if number >= 0:
    print (number, "is positive")
else:
    print (number, "is negative")


# Check number is even or odd

number = int(input("Check number is even or odd, Enter any number: "))

check_number = number % 2
if check_number == 0:
    print (number, "is even")
else:
    print (number, "is odd")


# Write a program to calculate the profit or loss

Cost_price = int(input("Enter Cost_price: "))
Sell_price = int(input("Enter Sell_price: "))

calculate_price = Sell_price - Cost_price

if calculate_price == 0:
    print ("Seller generate no profit no loss.")
elif calculate_price > 0:
    print ("Seller has made ", calculate_price, "Rs Profit.")
else:
    print ("Seller loss", calculate_price,"Rs")


# Taking marks of student and calculate the grade of the student

Student_marks = int(input("Enter Your Marks: "))

if Student_marks > 100:
    print ("Plz enter your correct marks")
elif Student_marks >= 81:
    print ("Student Grade: Very Good")
elif Student_marks >= 61:
    print ("Student Grade: Good")
elif Student_marks >= 40:
    print ("Student Grade: Average")
else:
    print ("Student Grade: Fail")